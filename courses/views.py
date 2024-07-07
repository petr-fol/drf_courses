from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from courses.models import Course, Material
from courses.serializers import CourseSerializer, MaterialSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class MaterialCreateAPIView(CreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialListAPIView(ListAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialRetrieveAPIView(RetrieveAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialUpdateAPIView(UpdateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialDestroyAPIView(DestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
