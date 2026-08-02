"""
Section blocks are full-width, visually prominent page sections
(heroes, promos, featured content). They inherit from BaseBlock
to get consistent block structure and template rendering.
"""

from django.utils.translation import gettext_lazy as _
from wagtail.blocks import CharBlock, PageChooserBlock, RichTextBlock
from wagtail.images.blocks import ImageChooserBlock

from .base_blocks import BaseBlock


class HeroBlock(BaseBlock):
    """
    Full-width hero banner with an image, title, body text, and a CTA link.
    """

    image = ImageChooserBlock(required=True, label=_("Image"))
    eyebrow = CharBlock(required=False, label=_("Eyebrow/Tag"))
    title = CharBlock(required=False, label=_("Title"))
    text = CharBlock(required=False, label=_("Text"))
    cta = CharBlock(required=False, label=_("Call to action label"))
    cta_link = PageChooserBlock(required=False, label=_("Call to action page"))

    class Meta:
        icon = "image"
        template = "section/hero_block.html"
        label = _("Hero")
        group=_("Section")


class PromoBlock(BaseBlock):
    """
    Promotional section with an image and rich-text body.
    """

    image = ImageChooserBlock(required=True, label=_("Image"))
    title = CharBlock(required=False, label=_("Title"))
    text = RichTextBlock(
        required=False,
        label=_("Text"),
        help_text=_("Write some promotional copy"),
    )

    class Meta:
        icon = "image"
        template = "section/promo_block.html"
        label = _("Promo")
        group=_("Section")


class FeaturedSectionBlock(BaseBlock):
    """
    Highlights a section of the site by linking to a parent page and
    displaying up to three of its children.
    """

    title = CharBlock(required=False, label=_("Title"))
    section = PageChooserBlock(
        required=False,
        label=_("Featured section"),
        help_text=_("Will display up to three child items."),
    )

    class Meta:
        icon = "image"
        template = "section/featured_section_block.html"
        label = _("Featured section")
        group=_("Section")
