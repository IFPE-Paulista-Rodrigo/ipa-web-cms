from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

from webaup.base.models import FooterText, Person
from webaup.products.models import Country


"""
N.B. To see what icons are available for use in Wagtail menus and StreamField block types,
enable the styleguide in settings:

INSTALLED_APPS = (
   ...
   'wagtail.contrib.styleguide',
   ...
)

or see https://thegrouchy.dev/general/2015/12/06/wagtail-streamfield-icons.html

This demo project includes the full font-awesome set via CDN in base.html, so the entire
font-awesome icon set is available to you. Options are at https://fontawesome.com/icons .
"""



class ProductCountryAdmin(ModelAdmin):
    model = Country
    search_fields = ("title",)



class PersonModelAdmin(ModelAdmin):
    model = Person
    menu_label = "People"  # ditch this to use verbose_name_plural from model
    menu_icon = "fa-users"  # change as required
    list_display = ("first_name", "last_name", "job_title", "thumb_image")
    list_filter = ("job_title",)
    search_fields = ("first_name", "last_name", "job_title")
    inspect_view_enabled = True


class FooterTextAdmin(ModelAdmin):
    model = FooterText
    search_fields = ("body",)


# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:



