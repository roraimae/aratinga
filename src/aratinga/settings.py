import os
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class _DefaultSettings:
    CMS_THEME = "Bootstrap"
    CMS_DISABLE_LAYOUT = False
    CMS_DISABLE_NAVBAR = False
    CMS_DISABLE_FOOTER = False
    
    THEMES_PATH = os.path.join(settings.BASE_DIR, 'themes')

    CMS_FRONTEND_BTN_SIZE_DEFAULT = ""
    CMS_FRONTEND_BTN_SIZE_CHOICES = [
        ("btn-sm", "Small"),
        ("", "Default"),
        ("btn-lg", "Large"),
    ]

    CMS_FRONTEND_BTN_STYLE_DEFAULT = "btn-primary"
    CMS_FRONTEND_BTN_STYLE_CHOICES = [
        ("btn-primary", "Primary"),
        ("btn-secondary", "Secondary"),
        ("btn-success", "Success"),
        ("btn-danger", "Danger"),
        ("btn-warning", "Warning"),
        ("btn-info", "Info"),
        ("btn-link", "Link"),
        ("btn-light", "Light"),
        ("btn-dark", "Dark"),
        ("btn-outline-primary", "Outline Primary"),
        ("btn-outline-secondary", "Outline Secondary"),
        ("btn-outline-success", "Outline Success"),
        ("btn-outline-danger", "Outline Danger"),
        ("btn-outline-warning", "Outline Warning"),
        ("btn-outline-info", "Outline Info"),
        ("btn-outline-light", "Outline Light"),
        ("btn-outline-dark", "Outline Dark"),
    ]

    
    CMS_FRONTEND_COL_SIZE_DEFAULT = ""
    CMS_FRONTEND_COL_SIZE_CHOICES = [
        ("", "Automatically size"),
        ("12", "Full row"),
        ("6", "Half - 1/2 column"),
        ("4", "Thirds - 1/3 column"),
        ("8", "Thirds - 2/3 column"),
        ("3", "Quarters - 1/4 column"),
        ("9", "Quarters - 3/4 column"),
        ("2", "Sixths - 1/6 column"),
        ("10", "Sixths - 5/6 column"),
        ("1", "Twelfths - 1/12 column"),
        ("5", "Twelfths - 5/12 column"),
        ("7", "Twelfths - 7/12 column"),
        ("11", "Twelfths - 11/12 column"),
    ]


    CMS_FRONTEND_COL_BREAK_DEFAULT = "md"
    CMS_FRONTEND_COL_BREAK_CHOICES = [
        ("", "Always expanded"),
        ("sm", "sm - Expand on small screens (phone, 576px) and larger"),
        ("md", "md - Expand on medium screens (tablet, 768px) and larger"),
        ("lg", "lg - Expand on large screens (laptop, 992px) and larger"),
        ("xl", "xl - Expand on extra large screens (wide monitor, 1200px)"),
    ]

    CMS_FRONTEND_TEMPLATES_PAGES = {
        # templates that are available for all page types
        "*": [
            (
                "",
                _("Default"),
            ),
            (
                "website/web_page.html",
                _("Web page showing title and cover image"),
            ),
            (
                "website/web_page_notitle.html",
                _("Web page without title and cover image"),
            ),
            (
                "website/home_page.html",
                _("Home page without title and cover image"),
            ),
            (
                "website/base.html",
                _("Blank page - no navbar or footer"),
            ),
        ],
    }

    CMS_PROTECTED_MEDIA_URL = "/protected/"
    CMS_PROTECTED_MEDIA_ROOT = os.path.join(settings.BASE_DIR, "protected")
    CMS_PROTECTED_MEDIA_UPLOAD_WHITELIST = []
    CMS_PROTECTED_MEDIA_UPLOAD_BLACKLIST = [
        ".app",
        ".bat",
        ".exe",
        ".jar",
        ".php",
        ".pl",
        ".ps1",
        ".py",
        ".rb",
        ".sh",
    ]

    CMS_FRONTEND_TEMPLATES_BLOCKS = {
        "cardblock": [
            (
                "aratinga/blocks/card_block.html",
                "Card",
            ),
            (
                "aratinga/blocks/card_head.html",
                "Card with header",
            ),
            (
                "aratinga/blocks/card_foot.html",
                "Card with footer",
            ),
            (
                "aratinga/blocks/card_head_foot.html",
                "Card with header and footer",
            ),
            (
                "aratinga/blocks/card_blurb.html",
                "Blurb - rounded image and no border",
            ),
            (
                "aratinga/blocks/card_img.html",
                "Cover image - use image as background",
            ),
        ],
        "cardgridblock": [
            (
                "aratinga/blocks/cardgrid_group.html",
                "Card group - attached cards of equal size",
            ),
            (
                "aratinga/blocks/cardgrid_deck.html",
                "Card deck - separate cards of equal size",
            ),
            (
                "aratinga/blocks/cardgrid_columns.html",
                "Card masonry - fluid brick pattern",
            ),
        ],
        # templates that are available for all block types
        "*": [
            ("", "Default"),
        ],
    }

    CMS_FRONTEND_TEMPLATES_PAGES = {
        # templates that are available for all page types
        "*": [
            (
                "",
                "Default",
            ),
            (
                "aratinga/pages/web_page.html",
                "Web page showing title and cover image",
            ),
            (
                "aratinga/pages/web_page_notitle.html",
                "Web page without title and cover image",
            ),
            (
                "aratinga/pages/home_page.html",
                "Home page without title and cover image",
            ),
            (
                "aratinga/pages/base.html",
                "Blank page - no navbar or footer",
            ),
        ],
    }

    def __getattribute__(self, attr: str):
        # First load from Django settings.
        # If it does not exist, load from _DefaultSettings.
        try:
            return getattr(settings, attr)
        except AttributeError:
            return super().__getattribute__(attr)


cms_settings = _DefaultSettings()