from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite
from reviews.models import (Publisher, Contributor, Book, BookContributor, Review)

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    search_fields = ['last_names', 'first_names']
    list_filter = ['last_names']


# admin_site = BookrAdminSite(name='bookr')

# Register your models here.
admin.site.register(Publisher)
# admin.site.register(Contributor)
admin.site.register(Book)
admin.site.register(BookContributor)
admin.site.register(Review)
admin.site.register(Contributor, ContributorAdmin)