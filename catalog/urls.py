from django.urls import path
from . import views
from .apps import CatalogConfig
from .views import ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('<int:pk>/catalog', ProductDetailView.as_view(), name='product')
]
