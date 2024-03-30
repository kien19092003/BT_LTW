from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import book_detail

urlpatterns = [
    path('', views.welcome_view, name='welcome_view'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('book-search', views.book_search, name='book_search'),
    path("publishers/<int:pk>/", views.publisher_edit, name="publisher_edit"),
    path("publishers/new/", views.publisher_edit, name="publisher_create"),
    path("books/<int:book_pk>/reviews/new/", views.review_edit, name="review_create"),
    path("books/<int:book_pk>/reviews/<int:review_pk>/", views.review_edit, name="review_edit"),
    path('books/<int:book_pk>/media/', views.book_media, name='book_media'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
