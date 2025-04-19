from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Bem-vindo à API ChaveCerta!</h1>
        <p>Acesse a documentação da nossa API:</p>
        <ul>
            <li><a href='/api/swagger/'>Swagger UI</a></li>
            <li><a href='/api/redoc/'>ReDoc</a></li>
        </ul>
    """)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),

    # Autenticação
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    
    # APIs
    path('api/imovel/', include('property.urls')),
    path('api/user/', include('user.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # Documentação automática
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # <-- Gera o esquema OpenAPI
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # <-- Swagger UI
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  # <-- Redoc UI
]

# Para servir arquivos estáticos e mídia no modo DEBUG
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
