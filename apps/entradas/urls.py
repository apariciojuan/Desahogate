"""webDe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

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
