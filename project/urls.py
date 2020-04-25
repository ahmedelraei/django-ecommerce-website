
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "e-Commerce Admin Panel"
admin.site.site_title = "eCommerce Admin Panel"
admin.site.index_title = "eCommerce Adminstration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('product.urls',namespace='products')),
    path('',include('accounts.urls',namespace='account')),
    path('accounts/', include('allauth.urls')),
    path('charts/',include('charts.urls',namespace='charts')),
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 