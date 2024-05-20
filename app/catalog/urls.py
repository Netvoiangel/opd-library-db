from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pdf/<int:pdf_id>/', views.pdf_view, name='pdf_view'),
    path('add/', views.add_pdf, name='add_pdf'),  # новый маршрут для добавления статьи
]
