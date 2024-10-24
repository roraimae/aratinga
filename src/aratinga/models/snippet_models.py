"""
Snippets are for content that is reusable in nature.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import InlinePanel
from wagtail.admin.panels import MultiFieldPanel
from wagtail.images import get_image_model_string
from wagtail.snippets.models import register_snippet
from wagtail.models import Orderable

from aratinga.blocks import HTML_STREAMBLOCKS
from wagtail.fields import StreamField


@register_snippet
class Carousel(ClusterableModel):
    """
    Model that represents a Carousel. Can be modified through the snippets UI.
    Selected through Page StreamField bodies by the CarouselSnippetChooser in
    snippet_choosers.py
    """

    class Meta:
        verbose_name = _("Carousel")

    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )
    show_controls = models.BooleanField(
        default=True,
        verbose_name=_("Show controls"),
        help_text=_(
            "Shows arrows on the left and right of the carousel to advance "
            "next or previous slides."
        ),
    )
    show_indicators = models.BooleanField(
        default=True,
        verbose_name=_("Show indicators"),
        help_text=_(
            "Shows small indicators at the bottom of the carousel based on the "
            "number of slides."
        ),
    )

    panels = [
        MultiFieldPanel(
            heading=_("Slider"),
            children=[
                FieldPanel("name"),
                FieldPanel("show_controls"),
                FieldPanel("show_indicators"),
            ],
        ),
        InlinePanel("carousel_slides", label=_("Slides")),
    ]

    def __str__(self):
        return self.name
    

class CarouselSlide(Orderable, models.Model):
    """
    Represents a slide for the Carousel model. Can be modified through the
    snippets UI.
    """

    class Meta(Orderable.Meta):
        verbose_name = _("Carousel Slide")

    carousel = ParentalKey(
        Carousel,
        related_name="carousel_slides",
        verbose_name=_("Carousel"),
    )
    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Image"),
    )
    background_color = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Background color"),
        help_text=_("Hexadecimal, rgba, or CSS color notation (e.g. #ff0011)"),
    )
    custom_css_class = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Custom CSS class"),
    )
    custom_id = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Custom ID"),
    )

    content = StreamField(
        HTML_STREAMBLOCKS,
        blank=True,
        use_json_field=True,
    )

    panels = [
        FieldPanel("image"),
        FieldPanel("background_color"),
        FieldPanel("custom_css_class"),
        FieldPanel("custom_id"),
        FieldPanel("content"),
    ]