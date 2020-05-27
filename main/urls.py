from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_view, name="home"),
    path('products/<slug:category_slug>/', views.product_list, name="product-list"),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name="product-detail"),
    path('catalog', views.PdfDownloadView.as_view(), name='catolog'),
    path('catalog/<slug:slug>/', views.pdf_view, name="catologview"),
    path('search/', views.SearchView.as_view(), name='search'),
    path('about-us/', TemplateView.as_view(template_name='about.html'), name="aboutus"),

]
