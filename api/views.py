from django.shortcuts import render
from rest_framework.response import Response
from api import models,serializer
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	UpdateAPIView,
	RetrieveUpdateAPIView,
	ListCreateAPIView,
	DestroyAPIView
	)
# Create your views here.

class StudentListView(ListCreateAPIView):
	queryset = models.Student.objects.all()
	serializer_class = serializer.Studentserializer


class StudentDetailView(RetrieveAPIView):
	queryset = models.Student.objects.all()
	serializer_class = serializer.Studentserializer

class StudentDeleteView(DestroyAPIView):
	queryset = models.Student.objects.all()
	serializer_class =serializer.Studentserializer