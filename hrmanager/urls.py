from django.urls import include, path
from django.contrib import admin
from rest_framework.authtoken import views
from employee.urls import employee_router


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include(employee_router.urls)),
    path("api-token-auth/", views.obtain_auth_token),
]
