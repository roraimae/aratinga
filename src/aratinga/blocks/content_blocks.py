"""
Content blocks are for building complex, nested HTML structures that usually
contain sub-blocks, and may require javascript to function properly.
"""

from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock

from .base_blocks import BaseBlock
from .base_blocks import CollectionChooserBlock
from .html_blocks import ButtonBlock

class CardBlock(BaseBlock):
    """
    A component of information with image, text, and buttons.
    """

    image = ImageChooserBlock(
        required=False,
        max_length=255,
        label=_("Image"),
    )
    title = blocks.CharBlock(
        required=False,
        max_length=255,
        label=_("Title"),
    )
    subtitle = blocks.CharBlock(
        required=False,
        max_length=255,
        label=_("Subtitle"),
    )
    description = blocks.RichTextBlock(
        features=["bold", "italic", "ol", "ul", "hr", "link", "document-link"],
        label=_("Body"),
    )
    links = blocks.StreamBlock(
        [("Links", ButtonBlock())],
        blank=True,
        required=False,
        label=_("Links"),
    )

    class Meta:
        template = "aratinga/blocks/card_foot.html"
        icon = "ara-list-alt"
        label = _("Card")


class CarouselBlock(BaseBlock):
    """
    Enables choosing a Carousel snippet.
    """

    carousel = SnippetChooserBlock("aratinga.Carousel")

    class Meta:
        icon = "image"
        label = _("Carousel")
        template = "aratinga/blocks/carousel_block.html"


class ImageGalleryBlock(BaseBlock):
    """
    Show a collection of images with interactive previews that expand to
    full size images in a modal.
    """

    collection = CollectionChooserBlock(
        required=True,
        label=_("Image Collection"),
    )

    class Meta:
        template = "aratinga/blocks/image_gallery_block.html"
        icon = "image"
        label = _("Image Gallery")