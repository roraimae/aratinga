"""
Create or customize your page models here.
"""

from aratinga.models import AratingaArticlePage

class ArticlePage(AratingaArticlePage):
    """
    Article, suitable for news or blog content.
    """

    class Meta:
        verbose_name = "Article"
        ordering = ["-first_published_at"]

    # Only allow this page to be created beneath an ArticleIndexPage.
    parent_page_types = ["website.ArticleIndexPage"]

    template = "aratinga/pages/article_page.html"
    search_template = "aratinga/pages/article_page.search.html"