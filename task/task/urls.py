
from django.contrib import admin
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from task.views import LogList

schema_view = get_schema_view(
   openapi.Info(
      title="NginxLog API",
      default_version='v1',
      description="This is documentation about NginxLog API",
      contact=openapi.Contact(email="riabova.ksenija@yandex.ru"),
   ),
   public=False,
   permission_classes=(permissions.IsAuthenticated,),
)





urlpatterns = [
    path('admin/', admin.site.urls),
    path('log_all/', LogList.as_view(), name='get-log-all'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
