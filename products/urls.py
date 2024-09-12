from django.urls import path

from products.views import products, baskets_add, baskets_remove

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:category_id>', products, name='category'),
    path('page/<int:page_number>', products, name='paginator'),
    path('baskets/add/<int:product_id>/', baskets_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', baskets_remove, name='baskets_remove'),
]