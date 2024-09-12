from django.urls import path

from products.views import ProductListView, baskets_add, baskets_remove

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('category/<int:category_id>', ProductListView.as_view(), name='category'),
    path('baskets/add/<int:product_id>/', baskets_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', baskets_remove, name='baskets_remove'),
]