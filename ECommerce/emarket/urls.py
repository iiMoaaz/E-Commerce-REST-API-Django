from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('product.urls')),
    path('api/', include('account.urls')),
    path('api/', include('order.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
]

handler404 = 'utils.error_view.handler404'
handler500 = 'utils.error_view.handler500'
