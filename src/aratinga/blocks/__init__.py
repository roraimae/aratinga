"""
Blocks module entry point. Used to cleanly organize blocks into
individual files based on purpose, but provide them all as a
single `blocks` module.
"""

from django.utils.translation import gettext_lazy as _
from wagtail import blocks


from .content_blocks import CardBlock
from .content_blocks import CarouselBlock

from .html_blocks import ButtonBlock
from .html_blocks import DownloadBlock
from .html_blocks import EmbedGoogleMapBlock
from .html_blocks import EmbedVideoBlock
from .html_blocks import ImageBlock
from .html_blocks import ImageLinkBlock
from .html_blocks import PageListBlock
from .html_blocks import PagePreviewBlock
from .html_blocks import QuoteBlock
from .html_blocks import RichTextBlock
from .html_blocks import TableBlock

from .layout_blocks import GridBlock
from .layout_blocks import CardGridBlock

# Collections of blocks commonly used together.

HTML_STREAMBLOCKS = [
    ("text", RichTextBlock(icon="ara-font")),
    ("button", ButtonBlock()),
    ("image", ImageBlock()),
    ("image_link", ImageLinkBlock()),
    (
        "html",
        blocks.RawHTMLBlock(
            icon="code",
            form_classname="monospace",
            label=_("HTML"),
        ),
    ),
    ("download", DownloadBlock()),
    ("embed_video", EmbedVideoBlock()),
    ("quote", QuoteBlock()),
    ("table", TableBlock()),
    ("google_map", EmbedGoogleMapBlock()),
    ("page_list", PageListBlock()),
    ("page_preview", PagePreviewBlock()),
]

CONTENT_STREAMBLOCKS = HTML_STREAMBLOCKS + [
    ("card", CardBlock()),
    ("carousel", CarouselBlock()),
]

LAYOUT_STREAMBLOCKS = [
    ("row", GridBlock(CONTENT_STREAMBLOCKS)),
    (
        "cardgrid",
        CardGridBlock(
            [
                ("card", CardBlock()),
            ]
        ),
    ),
    (
        "html",
        blocks.RawHTMLBlock(
            icon="code", form_classname="monospace", label="HTML"
        ),
    ),
]

STREAMFORM_BLOCKS = []