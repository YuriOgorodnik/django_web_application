from django.urls import path
from . import views
from .apps import CatalogConfig
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    VersionCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('', ProductListView.as_view(), name='list'),
    path('contacts/', views.contacts, name='contacts'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('version/create/<int:pk>/', VersionCreateView.as_view(), name='version_create'),
]
