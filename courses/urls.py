from django.urls import path
from rest_framework.routers import SimpleRouter

from courses.apps import CourseConfig
from courses.views import (CourseViewSet, MaterialCreateAPIView,
                           MaterialDestroyAPIView, MaterialListAPIView,
                           MaterialRetrieveAPIView, MaterialUpdateAPIView)

app_name = CourseConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("materials/", MaterialListAPIView.as_view(), name="materials_list"),
    path("materials/create/", MaterialCreateAPIView.as_view(), name="materials_create"),
    path(
        "materials/<int:pk>/",
        MaterialRetrieveAPIView.as_view(),
        name="materials_detail",
    ),
    path(
        "materials/<int:pk>/delete/",
        MaterialDestroyAPIView.as_view(),
        name="materials_delete",
    ),
    path(
        "materials/<int:pk>/update/",
        MaterialUpdateAPIView.as_view(),
        name="materials_update",
    ),
]


urlpatterns += router.urls
