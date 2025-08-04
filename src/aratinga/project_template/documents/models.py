
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.models import DraftStateMixin, Page, RevisionMixin

from django.template.defaulttags import register

from wagtail.documents.models import Document, AbstractDocument
from django.db import models

from wagtail.models import Collection
from aratinga.utils import clean_filters
from wagtail.search import index


class CustomDocument(AbstractDocument):

    description = models.TextField(max_length=255, verbose_name=("description"))

    admin_form_fields = Document.admin_form_fields + (
        # Add all custom fields names to make them appear in the form:
        'description',
    )

    search_fields = AbstractDocument.search_fields + [
        index.SearchField("description"),
    ]


class DocumentIndexPage(Page):

    class Meta:
        verbose_name = "Lista de Documentos"

    def get_documents(self):
        return (
            CustomDocument.objects.all()
        )

    def get_collections(self):
        collections = Collection.objects.get_indented_choices()
        collections_with_documents = []
        for item in collections:
            documents = CustomDocument.objects.filter(collection_id=item[0])
            if documents is not None:
                collections_with_documents.append({'collection__id':item[0], 'collection__name':item[1]})
        return collections_with_documents

    @register.filter
    def get_checked(dictionary, key):
        return dictionary.get(key)

    def paginate(self, request, *args):
        documents = self.get_documents()
        try:
            collection = Collection.objects.get(id=request.GET.get("collection"))
        except Collection.DoesNotExist:
            collection = None
        filters = {
            "title__icontains": request.GET.get("title"),
            "collection__path__icontains": collection.path if collection else None
        }
        filters = clean_filters(filters)
        documents = documents.filter(**filters)
        page = request.GET.get("page")
        paginator = Paginator(documents, 20)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    # Returns the above to the get_context method that is used to populate the
    # template
    def get_context(self, request):
        context = super(DocumentIndexPage, self).get_context(request)
        documents = self.paginate(request, self.get_documents())
        context["documents"] = documents
        return context

