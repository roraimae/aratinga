"""
Blocks module entry point. Used to cleanly organize blocks into
individual files based on purpose, but provide them all as a
single `blocks` module.
"""

from django.utils.translation import gettext_lazy as _
from wagtail import blocks

from .content_blocks import (
    CardBlock,
    CarouselBlock
)

from .html_blocks import (
    ButtonBlock,
    DownloadBlock,
    EmbedGoogleMapBlock,
    EmbedVideoBlock,
    ImageBlock,
    ImageLinkBlock,
    PageListBlock,
    PagePreviewBlock,
    QuoteBlock,
    RichTextBlock,
    TableBlock
)

from .layout_blocks import (
    GridBlock,
    CardGridBlock
)

from .section_blocks import (
    HeroBlock,
    PromoBlock,
    FeaturedSectionBlock
)

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
            label="HTML",
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

SECTION_STREAMBLOCKS = [
    ("hero", HeroBlock()),
    ("promo", PromoBlock()),
    ("featured_section", FeaturedSectionBlock()),
]

COMPONENT_STREAMBLOCKS = [
    ("content", blocks.StreamBlock(CONTENT_STREAMBLOCKS)),
    ("section", blocks.StreamBlock(SECTION_STREAMBLOCKS)),
]