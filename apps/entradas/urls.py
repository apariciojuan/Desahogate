from django.urls import path
from .views import *

app_name = 'entradas'

urlpatterns = [
    path('', index_views.as_view(), name='index'),
    path('tags/<slug:tag_slug>/', tags_list, name='tags_list_view'),
    path('Records/', up_Record_views.as_view(), name='up_records'),
    path('Record/<slug:slug>/', Record_views.as_view(), name='record_view'),
    path('Record/Edit/<slug:slug>/', Record_edit_views.as_view(), name='record_edit_view'),
]
