from django.contrib import admin
from django.urls import path
from cars.views import CarListView, CarUpdateView, CarCreateView

app_name = 'cars'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CarListView.as_view(), name='car_list'),
    path('car/create/', CarCreateView.as_view(), name='car_create'),
    path('car/update/<int:pk>/', CarUpdateView.as_view(), name='car_update'),
]
