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
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)


@register_setting(icon="cog")
class GenericSettings(ClusterableModel, BaseGenericSetting):
    twitter_url = models.URLField(verbose_name="Twitter URL", blank=True)
    github_url = models.URLField(verbose_name="GitHub URL", blank=True)
    organisation_url = models.URLField(verbose_name="Organisation URL", blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("github_url"),
                FieldPanel("twitter_url"),
                FieldPanel("organisation_url"),
            ],
            "Social settings",
        )
    ]


@register_setting(icon="site")
class SiteSettings(BaseSiteSetting):
    title_suffix = models.CharField(
        verbose_name="Title suffix",
        max_length=255,
        help_text="The suffix for the title meta tag e.g. ' | The Wagtail Bakery'",
        default="The Wagtail Bakery",
    )

    panels = [
        FieldPanel("title_suffix"),
    ]


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
      