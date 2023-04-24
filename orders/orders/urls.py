from django.contrib import admin
from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from shop.views import PartnerUpdate, RegisterAccount, LoginAccount, CategoryView, ShopView, ProductInfoView, \
    BasketView, AccountDetails, ContactView, OrderView, PartnerState, PartnerOrders, ConfirmAccount


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('api/v1/partner/state', PartnerState.as_view(), name='partner-state'),
    path('api/v1/partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    path('api/v1/user/register', RegisterAccount.as_view(), name='user-register'),
    path('api/v1/user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('api/v1/user/details', AccountDetails.as_view(), name='user-details'),
    path('api/v1/user/contact', ContactView.as_view(), name='user-contact'),
    path('api/v1/user/login', LoginAccount.as_view(), name='user-login'),
    path('api/v1/user/password_reset', reset_password_request_token, name='password-reset'),
    path('api/v1/user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
    path('api/v1/categories', CategoryView.as_view(), name='categories'),
    path('api/v1/shops', ShopView.as_view(), name='shops'),
    path('api/v1/products', ProductInfoView.as_view(), name='shops'),
    path('api/v1/basket', BasketView.as_view(), name='basket'),
    path('api/v1/order', OrderView.as_view(), name='order'),

]