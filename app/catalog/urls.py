from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pdf/<int:pdf_id>/', views.pdf_view, name='pdf_view'),
    path('add/', views.add_pdf, name='add_pdf'),  # новый маршрут для добавления статьи
    path('pdf/<int:pdf_id>/delete/', views.delete_pdf, name='delete_pdf'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
]
