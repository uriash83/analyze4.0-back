
from django.contrib import admin
from django.urls import path,include
from factors.apis import router
from .views import login


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('rest-auth/login/',login),
    path('rest-auth/', include('rest_auth.urls')), #auth and register
    path('rest-auth/registration/', include('rest_auth.registration.urls')),#register
    path('api/factors/', include(router.urls)),
    #path('api/factors/',include('factors.api.urls'))
]
