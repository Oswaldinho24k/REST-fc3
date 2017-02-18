from rest_framework import serializers
from ..models import Subject, Course
from django.contrib.auth.models import User


class SubjectSerializer(serializers.ModelSerializer):

	class Meta:
		model = Subject
		fields = ('id', 'title', 'slug', 'courses')

class CourseSerializer(serializers.ModelSerializer):

	class Meta:
		model = Course
		fields = ('id', 'subject', 'alumni')

class AlumniSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'username')

class CursoSerializer(serializers.ModelSerializer):

	subject = SubjectSerializer(many=False, read_only=True)
	alumni = AlumniSerializer(many=True, read_only=True)

	class Meta:
		model = Course
		fields = ('id', 'subject', 'alumni')

