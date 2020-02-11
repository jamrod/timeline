from django.urls import path
from . import views

urlpatterns = [
    path('', views.timeline_list, name='timeline_list'),
    path('timeline/<int:pk>', views.timeline_detail, name='timeline_detail'),
    path('timeline/<int:pk>/new', views.timeline_create, name='timeline_create'),
    path('timeline/<int:pk>/edit', views.timeline_edit, name='timeline_edit'),
    path('timeline/<int:pk>/delete', views.timeline_delete, name='timeline_delete'),
    path('capsule/', views.capsule_list, name='capsule_list'),
    path('capsule/<int:pk>', views.capsule_detail, name='capsule_detail'),
    path('capsule/<int:pk>/new', views.capsule_create, name='capsule_create'),
    path('capsule/<int:pk>/edit', views.capsule_edit, name='capsule_edit'),
    path('capsule/<int:pk>/delete', views.capsule_delete, name='capsule_delete')
]
