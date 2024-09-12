from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.shortcuts import redirect


def homeView(request):
    return redirect('swagger-ui')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('custom_auth.urls')),
    path('products/', include('products.urls')),
    path('', homeView),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]




