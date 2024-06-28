from django.urls import path
from . import views

app_name='to_do'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:do_id>/detail/', views.detail, name='detail'),
    path('<int:do_id>/modify/', views.modify, name='modify'),
    path('<int:do_id>/delete/', views.delete, name='delete'),
    path('addDo/', views.addDo, name='addDo'),
]