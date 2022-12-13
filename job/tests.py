"""Tests for Job App."""

from django.test import TestCase

from job.models import Category


class CategoryTestCase(TestCase):
    """Run tests for Tech Areas."""

    def setUp(self):
        """Setups a test case."""
        Category.objects.create(name='Desenvolvimento', code='DEV')

    def test_category_by_code(self):
        """Get a category by code."""
        area = Category.objects.get(code='DEV')
        self.assertEqual(area.name, 'Desenvolvimento')
