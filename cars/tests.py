from django.test import TestCase
from django.urls import reverse
from .models import Car

class CarModelTestCase(TestCase):
    def test_create(self):
        Car.objects.create(
            make="Honda",
            model="Accord",
            year=2017,
            )

class CarViewTestCase(TestCase):
    def setUp(self):
        self.data = {
            "make": "Jeep",
            "model": "Wrangler",
            "year": 2018,
        }
        self.car_1 = Car.objects.create(
            make="Honda",
            model="Accord",
            year=2017,
            )
        self.car_2 = Car.objects.create(
            make="Honda",
            model="Civic",
            year=2018,
            )
        self.car_3 = Car.objects.create(
            make="BMW",
            model="535",
            year=2015,
            )

    def test_list_view(self):
        list_url = reverse("car-list")
        response = self.client.get(list_url)
        for car in Car.objects.all():
            self.assertContains(response, car.make)
            self.assertContains(response, car.model)
        self.assertTemplateUsed(response, 'car_list.html')
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        detail_url = reverse("car-detail", kwargs={"car_id":self.car_1.id})
        response = self.client.get(detail_url)
        self.assertContains(response, self.car_1.make)
        self.assertContains(response, self.car_1.model)
        self.assertContains(response, self.car_1.year)
        self.assertTemplateUsed(response, 'car_detail.html')
        self.assertEqual(response.status_code, 200)

    def test_create_view(self):
        create_url = reverse("car-create")
        response = self.client.get(create_url)
        self.assertEqual(response.status_code, 200)
        response2 = self.client.post(create_url, self.data)
        self.assertEqual(response2.status_code, 302)

    def test_update_view(self):
        update_url = reverse("car-update", kwargs={"car_id":self.car_1.id})
        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(update_url, data=self.data)
        self.assertEqual(response.status_code, 302)

    def test_delete_view(self):
        delete_url = reverse("car-delete", kwargs={"car_id":self.car_1.id})
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 302)