from rest_framework import serializers
from api import models


class Instituteserializer(serializers.ModelSerializer):
	class Meta:
		model = models.Institute
		fiels = '__all__'

class Studentserializer(serializers.ModelSerializer):
	institute = Instituteserializer(read_only = True)
	class Meta:
		model = models.Student 
		fields = '__all__'