"""
Create or customize your page models here.
"""

from aratinga.models import AratingaArticlePage, AratingaArticleIndexPage, AratingaWebPage
from django.utils.translation import gettext_lazy as _

class ArticlePage(AratingaArticlePage):
    """
    Article, suitable for news or blog content.
    """

    class Meta:
        verbose_name = _("Article")
        ordering = ["-first_published_at"]

    # Only allow this page to be created beneath an ArticleIndexPage.
    parent_page_types = ["website.ArticleIndexPage"]

    template = "aratinga/pages/article_page.html"
    search_template = "aratinga/pages/article_page.search.html"


class ArticleIndexPage(AratingaArticleIndexPage):
    """
    Shows a list of article sub-pages.
    """

    class Meta:
        verbose_name = _("Article Landing Page")

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = "website.ArticlePage"

    # Only allow ArticlePages beneath this page.
    subpage_types = ["website.ArticlePage"]

    template = "aratinga/pages/article_index_page.html"


class WebPage(AratingaWebPage):
    """
    General use page with featureful streamfield.
    """

    class Meta:
        verbose_name = _("Web Page")

    template = "aratinga/pages/web_page.html"