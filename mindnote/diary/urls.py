from django.urls import path
from . import views

urlpatterns = [
    path('',views.page_list, name = 'page-list'),
    path('info/',views.info, name = 'info'),
    path('write/',views.page_create, name = 'page-create'),
    path('page/<int:page_id>/',views.page_detail, name = 'page-detail'),
    path('page/<int:page_id>/edit/',views.page_update, name = 'page-update'),
    # path('page/<int:page_id>/delete',views.page_delete, name = 'page-delete'),
]