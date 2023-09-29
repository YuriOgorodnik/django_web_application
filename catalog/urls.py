from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .apps import CatalogConfig
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    VersionCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('create/', login_required(ProductCreateView.as_view()), name='product_create'),
    path('', ProductListView.as_view(), name='list'),
    path('contacts/', views.contacts, name='contacts'),
    path('view/<int:pk>/', login_required(ProductDetailView.as_view()), name='product_view'),
    path('update/<int:pk>/', login_required(ProductUpdateView.as_view()), name='product_update'),
    path('delete/<int:pk>/', login_required(ProductDeleteView.as_view()), name='product_delete'),
    path('version/create/<int:pk>/', VersionCreateView.as_view(), name='version_create'),
]
