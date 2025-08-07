"""
Create or customize your page models here.
"""

from aratinga.models import AratingaPage, AratingaArticlePage, AratingaArticleIndexPage, AratingaWebPage
from django.utils.translation import gettext_lazy as _

class DefaultPage(AratingaPage):
    class Meta:
        verbose_name = _("Default Page")
        ordering = ["-first_published_at"]

    template = "aratinga/pages/page.html"
    search_template = "aratinga/pages/page.search.html"


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
        verbose_name = _("Article List Page")

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

    def get_context(self, request):
        context = super(WebPage, self).get_context(request)
        # featured = ArticlePage.objects.filter(featured=True).order_by('-date_published').first()
        last_news = ArticlePage.objects.all().order_by('-date_published')

        #if featured_article:
        #    last_news = last_news.exclude(id = featured_article.pk)

        #context['featured_article'] = featured_article
        context['last_news'] = last_news[:6]
        context['last_news_without_image'] = last_news[6:12]
        return context