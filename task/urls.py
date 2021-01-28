from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.all, name='all'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post')
]
