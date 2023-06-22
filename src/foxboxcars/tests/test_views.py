import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_car_list_view():
    client = Client()
    response = client.get(reverse('car_list'))
    assert response.status_code == 200
    assert any(template.name == 'cars/car_list.html' for template in response.templates)
    assert any(template.name == 'base.html' for template in response.templates)


@pytest.mark.django_db
def test_car_create_view():
    client = Client()
    response = client.get(reverse('car_create'))
    assert response.status_code == 200
    assert any(template.name == 'cars/car_create.html' for template in response.templates)
    assert any(template.name == 'base.html' for template in response.templates)


@pytest.mark.django_db
def test_car_update_view():
    client = Client()
    response = client.get(reverse('car_update'))
    assert response.status_code == 200
    assert any(template.name == 'cars/car_update.html' for template in response.templates)
    assert any(template.name == 'base.html' for template in response.templates)
