"""
Base and abstract pages used in Aratinga.
"""

import json
import logging
import os

from typing import TYPE_CHECKING

from django.utils.translation import gettext_lazy as _

from modelcluster.fields import ParentalKey

from taggit.models import TaggedItemBase

from wagtail.models import Page
from wagtail.models import PageBase

if TYPE_CHECKING:
    from wagtail.images.models import AbstractImage


CMS_PAGE_MODELS = []

def get_page_models():
    return CMS_PAGE_MODELS


class AratingaPageMeta(PageBase):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        if not cls._meta.abstract:
            CMS_PAGE_MODELS.append(cls)


class AratingaTag(TaggedItemBase):
    class Meta:
        verbose_name = _("CodeRed Tag")

    content_object = ParentalKey(
        "aratinga.AratingaPage", related_name="tagged_items"
    )


class AratingaPage(Page, metaclass=AratingaPageMeta):
    """
    General use page with templating functionality.
    All pages should inherit from this.
    """

    class Meta:
        verbose_name = _("Aratinga Page")

    # Do not allow this page type to be created in wagtail admin
    is_creatable = False