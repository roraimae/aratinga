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
        ("btn-sm", _("Small")),
        ("", _("Default")),
        ("btn-lg", _("Large")),
    ]

    CMS_FRONTEND_BTN_STYLE_DEFAULT = "btn-primary"
    CMS_FRONTEND_BTN_STYLE_CHOICES = [
        ("btn-primary", _("Primary")),
        ("btn-secondary", _("Secondary")),
        ("btn-success", _("Success")),
        ("btn-danger", _("Danger")),
        ("btn-warning", _("Warning")),
        ("btn-info", _("Info")),
        ("btn-link", _("Link")),
        ("btn-light", _("Light")),
        ("btn-dark", _("Dark")),
        ("btn-outline-primary", _("Outline Primary")),
        ("btn-outline-secondary", _("Outline Secondary")),
        ("btn-outline-success", _("Outline Success")),
        ("btn-outline-danger", _("Outline Danger")),
        ("btn-outline-warning", _("Outline Warning")),
        ("btn-outline-info", _("Outline Info")),
        ("btn-outline-light", _("Outline Light")),
        ("btn-outline-dark", _("Outline Dark")),
    ]

    
    CMS_FRONTEND_COL_SIZE_DEFAULT = ""
    CMS_FRONTEND_COL_SIZE_CHOICES = [
        ("", _("Automatically size")),
        ("12", _("Full row")),
        ("6", _("Half - 1/2 column")),
        ("4", _("Thirds - 1/3 column")),
        ("8", _("Thirds - 2/3 column")),
        ("3", _("Quarters - 1/4 column")),
        ("9", _("Quarters - 3/4 column")),
        ("2", _("Sixths - 1/6 column")),
        ("10", _("Sixths - 5/6 column")),
        ("1", _("Twelfths - 1/12 column")),
        ("5", _("Twelfths - 5/12 column")),
        ("7", _("Twelfths - 7/12 column")),
        ("11", _("Twelfths - 11/12 column")),
    ]


    CMS_FRONTEND_COL_BREAK_DEFAULT = "md"
    CMS_FRONTEND_COL_BREAK_CHOICES = [
        ("", _("Always expanded")),
        ("sm", _("sm - Expand on small screens (phone, 576px) and larger")),
        ("md", _("md - Expand on medium screens (tablet, 768px) and larger")),
        ("lg", _("lg - Expand on large screens (laptop, 992px) and larger")),
        ("xl", _("xl - Expand on extra large screens (wide monitor, 1200px)")),
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
                _("Card"),
            ),
            (
                "aratinga/blocks/card_head.html",
                _("Card with header"),
            ),
            (
                "aratinga/blocks/card_foot.html",
                _("Card with footer"),
            ),
            (
                "aratinga/blocks/card_head_foot.html",
                _("Card with header and footer"),
            ),
            (
                "aratinga/blocks/card_blurb.html",
                _("Blurb - rounded image and no border"),
            ),
            (
                "aratinga/blocks/card_img.html",
                _("Cover image - use image as background"),
            ),
        ],
        "cardgridblock": [
            (
                "aratinga/blocks/cardgrid_group.html",
                _("Card group - attached cards of equal size"),
            ),
            (
                "aratinga/blocks/cardgrid_deck.html",
                _("Card deck - separate cards of equal size"),
            ),
            (
                "aratinga/blocks/cardgrid_columns.html",
                _("Card masonry - fluid brick pattern"),
            ),
        ],
        # templates that are available for all block types
        "*": [
            ("", _("Default")),
        ],
    }

    CMS_FRONTEND_TEMPLATES_PAGES = {
        # templates that are available for all page types
        "*": [
            (
                "",
                _("Default"),
            ),
            (
                "aratinga/pages/web_page.html",
                _("Web page showing title and cover image"),
            ),
            (
                "aratinga/pages/web_page_notitle.html",
                _("Web page without title and cover image"),
            ),
            (
                "aratinga/pages/home_page.html",
                _("Home page without title and cover image"),
            ),
            (
                "aratinga/pages/base.html",
                _("Blank page - no navbar or footer"),
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