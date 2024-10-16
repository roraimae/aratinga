from wagtail import blocks
from aratinga.admin.settings import cms_settings

from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


class BaseBlock(blocks.StructBlock):
    """
    Common attributes for all blocks used in Aratinga CMS.
    """


    # placeholder, real value get set in __init__() from advsettings_class
    settings = blocks.Block()

    def __init__(self, local_blocks=None, **kwargs):
        """
        Construct and inject settings block, then initialize normally.
        """
        klassname = self.__class__.__name__.lower()
        choices = cms_settings.CMS_FRONTEND_TEMPLATES_BLOCKS.get(
            "*", []
        ) + cms_settings.CMS_FRONTEND_TEMPLATES_BLOCKS.get(klassname, [])

        if not local_blocks:
            local_blocks = ()

        local_blocks += (
            ("settings", self.advsettings_class(template_choices=choices)),
        )

        super().__init__(local_blocks, **kwargs)

    def render(self, value, context=None):
        template = value["settings"]["custom_template"]

        if not template:
            template = self.get_template(context=context)
            if not template:
                return self.render_basic(value, context=context)

        if context is None:
            new_context = self.get_context(value)
        else:
            new_context = self.get_context(value, parent_context=dict(context))

        return mark_safe(render_to_string(template, new_context))


class BaseLayoutBlock(BaseBlock):
    """
    Common attributes for all blocks used in Wagtail CRX.
    """

    # Subclasses can override this to provide a default list of blocks for the content.
    content_streamblocks = []

    def __init__(self, local_blocks=None, **kwargs):
        if not local_blocks and self.content_streamblocks:
            local_blocks = self.content_streamblocks

        if local_blocks:
            local_blocks = (
                (
                    "content",
                    blocks.StreamBlock(local_blocks, label=_("Content")),
                ),
            )

        super().__init__(local_blocks, **kwargs)
