from django.urls import path
from .views import Index, StoreView, Signup, Login, Cart, CheckOut, logout, OrderView
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name="homepage"),
    path('store', StoreView.as_view(), name="store"),
    path('signup', Signup.as_view(), name="signup"),
    path('login', Login.as_view(), name="login"),
    path('cart', auth_middleware(Cart.as_view()), name="cart"),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('logout', logout, name='logout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
