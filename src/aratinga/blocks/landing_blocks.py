"""
Landing page blocks provide the interactive and card-based components
needed to assemble institutional landing pages (alerts, stepper,
checklist, accordion/FAQ, anchor navigation, icon cards, link lists,
and contact cards).
"""

from django.utils.translation import gettext_lazy as _
from wagtail import blocks

from .base_blocks import BaseBlock
from .base_blocks import BaseLinkBlock


class AlertBlock(BaseBlock):
    """
    A callout/notice box with a colored style accent.
    """

    style = blocks.ChoiceBlock(
        choices=[
            ("info", _("Info")),
            ("success", _("Success")),
            ("warning", _("Warning")),
            ("danger", _("Danger")),
        ],
        default="info",
        required=False,
        label=_("Style"),
    )
    title = blocks.CharBlock(required=False, label=_("Title"))
    text = blocks.RichTextBlock(required=True, label=_("Text"))

    class Meta:
        icon = "warning"
        template = "blocks/alert_block.html"
        label = _("Alert")
        group = _("Interactive")


class StepBlock(BaseBlock):
    """
    A single step within a StepperBlock.
    """

    title = blocks.CharBlock(required=True, label=_("Step title"))
    text = blocks.TextBlock(required=False, label=_("Description"))


class StepperBlock(BaseBlock):
    """
    A numbered, step-by-step walkthrough.
    """

    steps = blocks.ListBlock(StepBlock(), label=_("Steps"))

    class Meta:
        icon = "order"
        template = "blocks/stepper_block.html"
        label = _("Stepper")
        group = _("Interactive")


class ChecklistBlock(BaseBlock):
    """
    A list of items with a check-mark bullet.
    """

    title = blocks.CharBlock(required=False, label=_("Title"))
    items = blocks.ListBlock(blocks.CharBlock(label=_("Item")), label=_("Items"))

    class Meta:
        icon = "tick"
        template = "blocks/checklist_block.html"
        label = _("Checklist")
        group = _("Interactive")


class AccordionPanelBlock(BaseBlock):
    """
    A single expandable panel within an AccordionBlock.
    """

    heading = blocks.CharBlock(required=True, label=_("Heading"))
    body = blocks.RichTextBlock(required=True, label=_("Content"))


class AccordionBlock(BaseBlock):
    """
    A list of expandable panels, e.g. for FAQs.
    """

    panels = blocks.ListBlock(AccordionPanelBlock(), label=_("Panels"))

    class Meta:
        icon = "help"
        template = "blocks/accordion_block.html"
        label = _("Accordion / FAQ")
        group = _("Interactive")


class AnchorNavItemBlock(blocks.StructBlock):
    """
    A single link within an AnchorNavBlock.
    """

    label = blocks.CharBlock(required=True, label=_("Label"))
    target = blocks.CharBlock(
        required=True, label=_("Anchor"), help_text=_("e.g. #faq")
    )


class AnchorNavBlock(BaseBlock):
    """
    An in-page navigation bar linking to anchors elsewhere on the page.
    """

    items = blocks.ListBlock(AnchorNavItemBlock(), label=_("Items"))

    class Meta:
        icon = "link"
        template = "blocks/anchor_nav_block.html"
        label = _("Anchor navigation")
        group = _("Interactive")


class IconCardBlock(BaseLinkBlock):
    """
    A card with an icon, title, description, and a link (page, document,
    or external URL).
    """

    icon = blocks.CharBlock(
        required=False,
        label=_("Icon"),
        help_text=_("Emoji or short text, e.g. \U0001F4DD"),
    )
    title = blocks.CharBlock(required=True, label=_("Title"))
    description = blocks.TextBlock(required=False, label=_("Description"))

    class Meta:
        icon = "site"
        template = "blocks/icon_card_block.html"
        label = _("Icon card")
        group = _("Content")


class LinkListBlock(BaseBlock):
    """
    A card with a title and a list of links, e.g. legislation or
    supporting materials.
    """

    title = blocks.CharBlock(required=True, label=_("Title"))
    links = blocks.ListBlock(BaseLinkBlock(), label=_("Links"))

    class Meta:
        icon = "list-ul"
        template = "blocks/link_list_block.html"
        label = _("Link list")
        group = _("Content")


class ContactItemBlock(blocks.StructBlock):
    """
    A single label/value pair within a ContactCardBlock.
    """

    label = blocks.CharBlock(
        required=True, label=_("Label"), help_text=_("e.g. Email")
    )
    value = blocks.CharBlock(required=True, label=_("Value"))
    link = blocks.CharBlock(
        required=False,
        label=_("Link (optional)"),
        help_text=_("e.g. mailto:contact@example.org or tel:+5511999999999"),
    )


class ContactCardBlock(BaseBlock):
    """
    A card of contact details (email, phone, address, etc).
    """

    title = blocks.CharBlock(required=True, label=_("Title"))
    items = blocks.ListBlock(ContactItemBlock(), label=_("Contact items"))

    class Meta:
        icon = "mail"
        template = "blocks/contact_card_block.html"
        label = _("Contact card")
        group = _("Content")
