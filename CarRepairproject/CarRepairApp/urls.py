from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='CarRepairApp-index'),
    path('about.html/', views.about, name='CarRepairApp-about'),
    path('contact.html/', views.contact, name='CarRepairApp-contact'),
    path('pricing.html/', views.pricing, name='CarRepairApp-pricing'),
    path('portfolio.html/', views.portfolio, name='CarRepairApp-portfolio'),
    path('services.html/', views.services, name='CarRepairApp-services'),
]