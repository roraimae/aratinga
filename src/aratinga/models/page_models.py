"""
Base and abstract pages used in Aratinga.
"""


from django.conf import settings

from django.db import models

from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from modelcluster.fields import ParentalKey

from taggit.models import TaggedItemBase

from wagtail.models import Page
from wagtail.models import PageBase
from wagtail.search import index
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import ObjectList
from wagtail.admin.panels import TabbedInterface
from wagtail.utils.decorators import cached_classmethod

from aratinga.settings import cms_settings
from aratinga.blocks import CONTENT_STREAMBLOCKS
from aratinga.blocks import LAYOUT_STREAMBLOCKS


CMS_PAGE_MODELS = []

def get_page_models():
    return CMS_PAGE_MODELS


class AratingaPageMeta(PageBase):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        if not cls._meta.abstract:
            CMS_PAGE_MODELS.append(cls)


class AratingaTag(TaggedItemBase):
    class Meta:
        verbose_name = _("Aratinga Tag")

    content_object = ParentalKey(
        "aratinga.AratingaPage", related_name="tagged_items"
    )


class AratingaPage(Page, metaclass=AratingaPageMeta):
    """
    General use page with templating functionality.
    All pages should inherit from this.
    """

    class Meta:
        verbose_name = _("Aratinga Page")

    # Do not allow this page type to be created in wagtail admin
    is_creatable = False

    # Subclasses can override these fields to enable custom
    # ordering based on specific subpage fields.
    index_order_by_default = ""
    index_order_by_choices = (
        ("", _("Default Ordering")),
        ("-first_published_at", _("Date first published, newest to oldest")),
        ("first_published_at", _("Date first published, oldest to newest")),
        ("-last_published_at", _("Date updated, newest to oldest")),
        ("last_published_at", _("Date updated, oldest to newest")),
        ("title", _("Title, alphabetical")),
        ("-title", _("Title, reverse alphabetical")),
    )

    index_order_by = models.CharField(
        max_length=255,
        choices=index_order_by_choices,
        default=index_order_by_default,
        blank=True,
        verbose_name=_("Order child pages by"),
        help_text=_("Child pages will then be sorted by this attribute."),
    )

    ###############
    # Layout fields
    ###############

    custom_template = models.CharField(
        blank=True, max_length=255, choices=None, verbose_name=_("Template")
    )

    ###############
    # Panels
    ###############

    body_content_panels = []

    bottom_content_panels = []

    layout_panels = []

    def __init__(self, *args, **kwargs):
        """
        Inject custom choices and defaults into the form fields
        to enable customization by subclasses.
        """
        super().__init__(*args, **kwargs)
        klassname = self.__class__.__name__.lower()
        template_choices = cms_settings.CMS_FRONTEND_TEMPLATES_PAGES.get(
            "*", []
        ) + cms_settings.CMS_FRONTEND_TEMPLATES_PAGES.get(klassname, [])

        self._meta.get_field(
            "index_order_by"
        ).choices = self.index_order_by_choices
        self._meta.get_field("custom_template").choices = template_choices
        if not self.id:
            self.index_order_by = self.index_order_by_default
    


    @cached_classmethod
    def get_edit_handler(cls):
        """
        Override to "lazy load" the panels overridden by subclasses.
        """
        panels = [
            ObjectList(
                cls.content_panels
                + cls.body_content_panels
                + cls.bottom_content_panels,
                heading=_("Content"),
            ),
            ObjectList(cls.layout_panels, heading=_("Layout")),
            ObjectList(
                cls.settings_panels, heading=_("Settings"), classname="settings"
            ),
        ]

        edit_handler = TabbedInterface(panels)
        return edit_handler.bind_to_model(cls)




###############################################################################
# Abstract pages providing pre-built common website functionality, suitable for subclassing.
# These are abstract so subclasses can override fields if desired.
###############################################################################

class AratingaWebPage(AratingaPage):
    """
    Provides a body and body-related functionality.
    This is abstract so that subclasses can override the body StreamField.
    """

    class Meta:
        verbose_name = _("Aratinga Web Page")
        abstract = True

    template = "aratinga/pages/web_page.html"

    # Child pages should override based on what blocks they want in the body.
    # Default is LAYOUT_STREAMBLOCKS which is the fullest editor experience.
    body = StreamField(
        LAYOUT_STREAMBLOCKS,
        null=True,
        blank=True,
        use_json_field=True,
    )

    # Search fields
    search_fields = AratingaPage.search_fields + [index.SearchField("body")]

    # Panels
    body_content_panels = [
        FieldPanel("body"),
    ]

    @property
    def body_preview(self):
        """
        A shortened version of the body without HTML tags.
        """
        # add spaces between tags for legibility
        body = str(self.body).replace(">", "> ")
        # strip tags
        body = strip_tags(body)
        # truncate and add ellipses
        preview = body[:200] + "..." if len(body) > 200 else body
        return mark_safe(preview)


class AratingaArticlePage(AratingaWebPage):
    """
    Article, suitable for news or blog content.
    """

    class Meta:
        verbose_name = _("Aratinga Article")
        abstract = True

    template = "website/article_page.html"
    search_template = "website/article_page.search.html"

    related_show_default = True

    # Override body to provide simpler content
    body = StreamField(
        CONTENT_STREAMBLOCKS,
        null=True,
        blank=True,
        use_json_field=True,
    )

    caption = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Caption"),
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        editable=True,
        on_delete=models.SET_NULL,
        verbose_name=_("Author"),
    )
    author_display = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Display author as"),
        help_text=_("Override how the author’s name displays on this article."),
    )
    date_display = models.DateField(
        null=True,
        blank=True,
        verbose_name=_("Display publish date"),
    )

class AratingaArticleIndexPage(AratingaWebPage):
    """
    Shows a list of article sub-pages.
    """

    class Meta:
        verbose_name = _("Aratinga Article Index Page")
        abstract = True

    template = "website/article_index_page.html"

    index_show_subpages_default = True

    index_order_by_default = "-date_display"
    index_order_by_choices = (
        ("-date_display", "Display publish date, newest first"),
    ) + AratingaWebPage.index_order_by_choices

    show_images = models.BooleanField(
        default=True,
        verbose_name=_("Show images"),
    )
    show_captions = models.BooleanField(
        default=True,
    )
    show_meta = models.BooleanField(
        default=True,
        verbose_name=_("Show author and date info"),
    )
    show_preview_text = models.BooleanField(
        default=True,
        verbose_name=_("Show preview text"),
    )