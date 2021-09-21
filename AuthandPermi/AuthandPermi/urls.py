from django.contrib import admin
from django.db import router
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# Creating Router object
router = DefaultRouter()


# Register StudentViewSet with Router
router.register('studentapi', views.StudentModelViewSet, basename='student')

#router.register('studentapi/<int:pk>', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
]
