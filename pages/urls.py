from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index,name='Index'),
    path('newSubject', views.createSubject,name='CreateSubject'),
    path('konu/<slug:slug>',views.subjectDetails,name='subjectDetails'),
    path('kategori/<slug:slug>',views.getCategory,name='category'),
    path('uye/<int:id>',views.userDetails,name='userDetails'),
    path('konu/sil/<int:id>',views.deleteTopic,name='deleteTopic'),
    path('search',views.search,name='search'),
    path('mesaj/sil/<int:id>',views.deleteComment,name='deleteComment'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
