"""
Blocks module entry point. Used to cleanly organize blocks into
individual files based on purpose, but provide them all as a
single `blocks` module.
"""

from django.utils.translation import gettext_lazy as _
from wagtail import blocks

from .content_blocks import (
    CardBlock,
    CarouselBlock,
    ImageGalleryBlock,
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

from .landing_blocks import (
    AccordionBlock,
    AlertBlock,
    AnchorNavBlock,
    ChecklistBlock,
    ContactCardBlock,
    IconCardBlock,
    LinkListBlock,
    StepperBlock,
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
    ("text", RichTextBlock()),
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
    ("image_gallery", ImageGalleryBlock()),
]

LAYOUT_STREAMBLOCKS = [
    ("row", GridBlock(CONTENT_STREAMBLOCKS)),
    (
        "cardgrid",
        CardGridBlock(
            [
                ("card", CardBlock()),
                ("icon_card", IconCardBlock()),
            ]
        ),
    ),
    (
        "html",
        blocks.RawHTMLBlock(
            icon="code", form_classname="monospace", label=_("HTML")
        ),
    ),
]

SECTION_STREAMBLOCKS = [
    ("hero", HeroBlock()),
    ("promo", PromoBlock()),
    ("featured_section", FeaturedSectionBlock()),
]

LANDING_STREAMBLOCKS = [
    ("alert", AlertBlock()),
    ("stepper", StepperBlock()),
    ("checklist", ChecklistBlock()),
    ("accordion", AccordionBlock()),
    ("anchor_nav", AnchorNavBlock()),
    ("icon_card", IconCardBlock()),
    ("link_list", LinkListBlock()),
    ("contact_card", ContactCardBlock()),
]

COMPONENT_STREAMBLOCKS = CONTENT_STREAMBLOCKS + SECTION_STREAMBLOCKS + LANDING_STREAMBLOCKS