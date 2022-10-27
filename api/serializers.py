"""Serializers for API App."""

from rest_framework import serializers

from job.models import Category, Company, Job


class CompanySerializer(serializers.ModelSerializer):
    """Company serializer."""

    class Meta(object):
        model = Company
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    """Category serializer."""

    class Meta(object):
        model = Category
        fields = ['id', 'name', 'code']


class JobSerializer(serializers.ModelSerializer):
    """Job serializer, with nested elements for category and company."""

    category = CategorySerializer(read_only=True)
    company = CompanySerializer(read_only=True)

    class Meta(object):
        model = Job
        fields = ['id', 'title', 'location', 'link', 'category', 'company']
