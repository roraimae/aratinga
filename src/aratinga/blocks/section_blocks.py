from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StructBlock,
    TextBlock,
    IntegerBlock,
    PageChooserBlock
)

from wagtail.images.blocks import ImageChooserBlock

class HeroBlock(StructBlock):

    # Hero section of HomePage
    image = ImageChooserBlock(required=True)
    hero_text = CharBlock(required=False)
    hero_cta =CharBlock(required=False)
    hero_cta_link = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "aratinga/section/hero_block.html"
        preview_value = {"attribution": "The Wagtail Bakery"}
        description = "An image with optional caption and attribution"

class PromoBlock(StructBlock):
    # Promo section of the HomePage
    promo_image = ImageChooserBlock(required=True)
    promo_title = CharBlock(required=False)
    promo_text = RichTextBlock(
        required=False, help_text="Write some promotional copy"
    )

    class Meta:
        icon = "image"
        template = "aratinga/section/promo_block.html"
        preview_value = {"attribution": "The Wagtail Bakery"}
        description = "An image with optional caption and attribution"


class ForeignKeyBlock(StructBlock):
    page_object_id = IntegerBlock(required=True)

    def get_related_object(self, value):
        return Page.objects.get(id=value["page_id"])


class FeaturedSectionBlock(StructBlock):
    # Featured sections on the HomePage
    # You will see on templates/base/home_page.html that these are treated
    # in different ways, and displayed in different areas of the page.
    # Each list their children items that we access via the children function
    # that we define on the individual Page models e.g. BlogIndexPage
    title = CharBlock(required=False)
    section = PageChooserBlock(required=False, help_text="Featured section for the homepage. Will display up to three child items.")

    class Meta:
        icon = "image"
        template = "aratinga/section/featured_section_block.html"
        preview_value = {"attribution": "The Wagtail Bakery"}
        description = "An image with optional caption and attribution"