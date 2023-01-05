from django.urls import path

from .views import (addcomment, shop_cart, 
                    home_page, 
                    category_product, 
                    product_detail,
                    add_to_cart,
                    remove_single_quantity_product,
                    remove_product_from_cart,
                    cart,
                    faq,
                    user_profile, user_update,search,
                    CheckoutView,ajax_variant
                    )

urlpatterns = [
    path('', home_page, name='home_page'),
    path('ajax_variant', ajax_variant, name='ajax_variant'),
    # product
    path('search', search, name='search'),
    path('faq', faq, name='faq'),
    path('category/<int:id>/<slug:slug>', 
                    category_product, name='category_product'),
    path('product/<int:id>/<slug:slug>', 
                    product_detail, name='product_detail'),
    path('product/addcomment/<int:id>', addcomment, name='addcomment'),
    path('addtocart/<int:id>', add_to_cart, name='addtocart'),
    path('remove-product-from-cart/<int:id>', remove_product_from_cart, name='remove-product-from-cart'),
    path('remove-single-quantity-product/<int:id>', 
                remove_single_quantity_product, 
                name='remove-single-quantity-product'),

    # order
    path('shopcart', shop_cart, name='shop-cart'),
    path('cart', cart, name='cart'),
    path('checkout', CheckoutView.as_view(), name='checkout'),

    # user
    path('userprofile', user_profile, name='user_profile'),
    path('userupdate', user_update, name='user_update'),

]