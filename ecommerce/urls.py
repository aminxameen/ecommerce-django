from django.urls import path, include
from .views import *


urlpatterns = [
    path('',index),
    path('login/',signIn),
    path('register/',register),
    path('shop/',shop),
    path('cart/',cart),
    path('wishlist/',wishlist),
    path('profile/',profile),
    
    path('logout/',user_logout),
    path('product/<int:id>',productDetails),
    path('remove-from-cart/<int:cart_id>',removeFromCart),

    path('add-to-cart/<int:product_id>',addToCart),
    path('add-to-wishlist/<int:product_id>',AddWishlist),
    path('remove-from-wishlist/<int:wishlist_id>',removeFromWishList),
    
    path('checkout/',checkout),
    path('order/', orderedItems),
    
# api urllls
    
    path('get-products',getProducts)
    
    
]
