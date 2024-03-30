from django.contrib import admin
from django.contrib.admin import AdminSite

class BookrAdminSite(AdminSite):
 title_header = 'Bookr Admin'
 site_header = 'Bookr administration'
 index_title = 'Bookr site admin'

# admin_site = BookrAdminSite(name='bookr')
