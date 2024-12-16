from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from django.core.paginator import EmptyPage
from django.core.paginator import InvalidPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator

from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType

from wagtail.models import Page
from wagtail.models import get_page_models
from wagtail.search.backends import get_search_backend
from wagtail.search.backends.database.mysql.mysql import MySQLSearchBackend


from aratinga.forms import SearchForm

from aratinga.templatetags.aratinga_tags import get_name_of_class
from aratinga.models import SiteSettings

from django.shortcuts import render, get_object_or_404
from .models.snippets_models import Template


def preview_template(request, template_id):
    template = get_object_or_404(Template, id=template_id)

    # Example dynamic rendering (context can be passed dynamically from GET/POST data)
    rendered_content = template.render(context={"user_name": request.user.username})

    return render(request, "pages/preview_template.html", {"rendered_content": rendered_content})


@login_required
@permission_required(
    "wagtailadmin.access_admin",
    login_url="wagtailadmin_login",
)
def import_index(request):
    """
    Landing page to replace wagtailimportexport.
    """
    return render(request, "wagtailimportexport/index.html")


def search(request):
    """
    Searches pages across the entire site.
    """
    search_form = SearchForm(request.GET)
    pagetypes = []
    results = None
    results_paginated = None

    if search_form.is_valid():
        search_query = search_form.cleaned_data["s"]
        search_model = search_form.cleaned_data["t"]

        # get all page models
        pagemodels = sorted(get_page_models(), key=get_name_of_class)
        # filter based on is search_filterable
        for model in pagemodels:
            if hasattr(model, "search_filterable") and model.search_filterable:
                pagetypes.append(model)

        results = Page.objects.live()
        if search_model:
            try:
                # If provided a model name, try to get it
                model = ContentType.objects.get(model=search_model).model_class()
                # Workaround for Wagtail MySQL search bug.
                # See: https://github.com/wagtail/wagtail/issues/11273
                backend = get_search_backend()
                if type(backend) is MySQLSearchBackend:
                    results = model.objects.live()
                else:
                    results = results.type(model)
            except ContentType.DoesNotExist:
                # Maintain existing behavior of only returning objects if the page type is real
                results = None

        # get and paginate results
        if results:
            results = results.search(search_query)
            paginator = Paginator(
                results, SiteSettings.for_request(request).search_num_results
            )
            page = request.GET.get("p", 1)
            try:
                results_paginated = paginator.page(page)
            except PageNotAnInteger:
                results_paginated = paginator.page(1)
            except EmptyPage:
                results_paginated = paginator.page(1)
            except InvalidPage:
                results_paginated = paginator.page(1)

    # Render template
    return render(
        request,
        "aratinga/pages/search.html",
        {
            "request": request,
            "pagetypes": pagetypes,
            "form": search_form,
            "results": results,
            "results_paginated": results_paginated,
        },
    )


def robots(request):
    return render(request, "robots.txt", content_type="text/plain")
