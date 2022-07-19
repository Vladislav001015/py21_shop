
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('applications.account.urls')),
    path('api/v1/product/', include('applications.product.urls'))
]
