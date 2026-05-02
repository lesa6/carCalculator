import pytest
from calculator import Car, ElectricCar, Calculator

@pytest.fixture
def car():
    print('\nCreating a new car\n')
    return Car('Toyota Corolla', price=120000, fuel_economy=7, service_cost=1200, insurance_cost=2500)

@pytest.fixture
def electric_car():
    print('\nCreating a new car\n')
    return ElectricCar('Tesla Model 3', 200000, 5500, 150)

@pytest.fixture
def calculator(car):
    res = Calculator()
    res.add_car(car)
    return res

@pytest.fixture
def password():
    return 'Jibhfr456'