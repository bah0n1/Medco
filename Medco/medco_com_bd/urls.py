from django.urls import path
from medco_com_bd import views
from django.conf import settings
from django.conf.urls.static import static
from .forms import MyPasswordResetForm,MySetPassword
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home.as_view(),name="home"),
    path('product-detail/<int:pk>', views.product_detail, name='product-detail'),


    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('plus_cart/', views.plus_cart, name='pluscart'),
    path('minus_cart/', views.minus_cart, name='minuscart'),
    path('remove_cart/', views.remove_cart, name='removecart'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('terms/', views.terms, name='terms'),
    path('search/', views.search, name='search'),
    path('autocompleted/', views.autocompleted, name='autocompleted'),
    
    
    
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.Profile_View.as_view(), name='profile'),
    
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
   
   
    path('allmedicine/<slug:data>', views.allmedicine, name='medicine'),
    path('allmedicine/', views.allmedicine, name='allmedicine'),



    path("password-reset/",
    auth_views.PasswordResetView.as_view(template_name="app/pass_res.html",form_class=MyPasswordResetForm),
    name="passwordreset"),
    
    #path("password-reset/done/",auth_views.PasswordResetDoneView.as_view(template_name="app/pass_res_don.html"),name="passwordresetdone"),
    
    #path("password-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="app/pass_res_confirm.html",form_class=MySetPassword),name="passwordresetconfirm"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="app/pass_res_don.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="app/pass_res_confirm.html",form_class=MySetPassword),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="app/pass_res_completed.html"),name='password_reset_complete'),
    
    #path("password-reset/complete/",auth_views.PasswordResetCompleteView.as_view(template_name="app/pass_res_completed.html"),name="passwordresetcompleted"),
    

    #address/profile  add/delete/edit

    path('address/', views.address, name='address'),
    path('address/<int:id>/', views.delete_ad, name='del_add'),
    path('address_ed/<int:pd>/', views.edit_ad, name='ed_add'),
    path("data/",views.data,name="data"),
    
    
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    #path('registration/', views.customerregistration, name='customerregistration'),
    path('registration/', views.customerregistration.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path("resend_otp/",views.resend_otp,name="resend_otp"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)