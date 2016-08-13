from django.conf.urls import url

from . import views

app_name = 'indee'
urlpatterns = [
    url(r'^$', views.index, name='document-listing'),
    url(r'^pdf/all', views.index, name='document-listing-1'),
    url(r'^pdf/upload', views.upload, name='upload'),
    url(r'^pdf/delete_documents', views.delete_documents, name='delete_documents_table'),
    url(r'^pdf/public/(?P<pdf_id>[0-9]+)', views.public_viewer, name='pdf_public_viewer'),
]