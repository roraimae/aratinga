from django.db import models
from django.utils.translation import gettext_lazy as _

from modelcluster.models import ClusterableModel

from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import InlinePanel
from wagtail.admin.panels import MultiFieldPanel


from wagtail.contrib.settings.models import BaseSiteSetting
from wagtail.contrib.settings.models import register_setting
from wagtail.images import get_image_model_string

from aratinga.settings import cms_settings


def conditional_register_setting(condition: bool, **kwargs):
    
    def decorator(cls):
        if not condition:
            register_setting(cls, **kwargs)
        return cls

    return decorator


@conditional_register_setting(cms_settings.CMS_DISABLE_LAYOUT, icon="cms-desktop")
class LayoutSettings(ClusterableModel, BaseSiteSetting):
    """
    Branding, navbar, and theme settings.
    """

    class Meta:
        verbose_name = _("CMS Settings")

    logo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Logo"),
        help_text=_("Brand logo used in the navbar and throughout the site"),
    )
    favicon = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="favicon",
        verbose_name=_("Favicon"),
    )
    navbar_color_scheme = models.CharField(
        blank=True,
        max_length=50,
        choices=None,
        default="",
        verbose_name=_("Navbar color scheme"),
        help_text=_(
            "Optimizes text and other navbar elements for use with light or "
            "dark backgrounds."
        ),
    )
    navbar_class = models.CharField(
        blank=True,
        max_length=255,
        default="",
        verbose_name=_("Navbar CSS class"),
        help_text=_(
            'Custom classes applied to navbar e.g. "bg-light", "bg-dark", "bg-primary".'
        ),
    )
    navbar_fixed = models.BooleanField(
        default=False,
        verbose_name=_("Fixed navbar"),
        help_text=_("Fixed navbar will remain at the top of the page when scrolling."),
    )
    navbar_content_fluid = models.BooleanField(
        default=False,
        verbose_name=_("Full width navbar contents"),
        help_text=_("Content within the navbar will fill edge to edge."),
    )
    navbar_collapse_mode = models.CharField(
        blank=True,
        max_length=50,
        choices=None,
        default="",
        verbose_name=_("Collapse navbar menu"),
        help_text=_(
            "Control on what screen sizes to show and collapse the navbar menu links."
        ),
    )
    navbar_format = models.CharField(
        blank=True,
        max_length=50,
        choices=None,
        default="",
        verbose_name=_("Navbar format"),
    )
    navbar_search = models.BooleanField(
        default=True,
        verbose_name=_("Search box"),
        help_text=_("Show search box in navbar"),
    )
    from_email_address = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_("From email address"),
        help_text=_(
            "The default email address this site appears to send from. "
            'For example: "sender@example.com" or '
            '"Sender Name <sender@example.com>" (without quotes)'
        ),
    )
    search_num_results = models.PositiveIntegerField(
        default=10,
        verbose_name=_("Number of results per page"),
    )
    external_new_tab = models.BooleanField(
        default=False, verbose_name=_("Open all external links in new tab")
    )
    google_maps_api_key = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_("Google Maps API Key"),
        help_text=_("The API Key used for Google Maps."),
    )
    mailchimp_api_key = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_("Mailchimp API Key"),
        help_text=_("The API Key used for Mailchimp."),
    )


    def __init__(self, *args, **kwargs):
        """
        Inject custom choices and defaults into the form fields
        to enable customization of settings without causing migration issues.
        """
        super().__init__(*args, **kwargs)
        # Set choices dynamically.
        self._meta.get_field(
            "navbar_collapse_mode"
        ).choices = cms_settings.CMS_FRONTEND_NAVBAR_COLLAPSE_MODE_CHOICES
        self._meta.get_field(
            "navbar_color_scheme"
        ).choices = cms_settings.CMS_FRONTEND_NAVBAR_COLOR_SCHEME_CHOICES
        self._meta.get_field(
            "navbar_format"
        ).choices = cms_settings.CMS_FRONTEND_NAVBAR_FORMAT_CHOICES
        # Set default dynamically.
        if not self.id:
            self.navbar_class = cms_settings.CMS_FRONTEND_NAVBAR_CLASS_DEFAULT
            self.navbar_collapse_mode = (
                cms_settings.CMS_FRONTEND_NAVBAR_COLLAPSE_MODE_DEFAULT
            )
            self.navbar_color_scheme = (
                cms_settings.CMS_FRONTEND_NAVBAR_COLOR_SCHEME_DEFAULT
            )
            self.navbar_format = cms_settings.CMS_FRONTEND_NAVBAR_FORMAT_DEFAULT
