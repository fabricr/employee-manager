# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from employee.models import Employee


class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.employee = {'name': 'Fabricio Machado',
                         'email': 'fabricio.renan@live.com',
                         'department':'E-Commerce'}
        self.response = self.client.post(
            reverse('create'),
            self.employee,
            format="json")

    def test_post_employee(self):

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_employee(self):
        employee = Employee.objects.get()
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': employee.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, employee)

    def test_delete_employee(self):
        employee = Employee.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': employee.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)