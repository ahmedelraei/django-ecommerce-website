# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns

admin.site.site_header = "Elraei Admin Panel"
admin.site.site_title = "Elraei Admin Panel"
admin.site.index_title = "Elraei Adminstration"

urlpatterns = [
    path('admin/', admin.site.urls),
    
] 
urlpatterns += i18n_patterns(
    path('',include('product.urls',namespace='products')),
    path('',include('clients.urls',namespace='clients')),
    path('designer/',include('designer.urls',namespace='designer')),
    path('accounts/', include('allauth.urls')),
    path('charts/',include('charts.urls',namespace='charts')),
    path('paypal/',include('paypal.standard.ipn.urls')),
    path('payment/',include('payment.urls',namespace='payment')),
    path('administration/',include('administration.urls',namespace='administration')),
    path('tinymce/', include('tinymce.urls')),
    path('api/', include('API.urls',namespace='API')),
    prefix_default_language=True,

)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 