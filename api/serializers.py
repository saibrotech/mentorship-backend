from rest_framework import serializers

from job.models import Category, Company, Job


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'code']


class JobSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'title', 'location', 'link', 'category', 'company']
