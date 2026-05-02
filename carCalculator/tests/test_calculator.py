from calculator import add_two_numbers, Car, ElectricCar
import pytest
import random
from apis import get_gas_price, get_power_price

data = [(10,15,0.67), (100, 50, 2), (4, 2, 2), (10, 0 , 0), (0, 5, 0)]
mileage = [1000, 10000, 20000]

class TestCar:
    def test_static_year_cost(self, car):
        res = car.static_year_cost()
        assert res == 3700
    
    @pytest.mark.parametrize('mileage', mileage)
    def test_dynamic_year_cost(self, car, mileage):
        res = car.dynamic_year_cost(mileage)
        expected = car.fuel_economy * mileage / 100 * get_gas_price()
        assert res ==  expected

    @pytest.mark.parametrize('mileage', mileage)
    def test_dynamic_year_cost(self, car, mileage):
        res = car.year_cost(mileage)
        expected = car.static_year_cost() + car.dynamic_year_cost(mileage)
        assert res == expected

class TestElectricCar:
    @pytest.mark.parametrize('mileage', mileage)
    def test_dynamic_year_cost(self, electric_car, mileage):
        res = electric_car.dynamic_year_cost(mileage)
        expected = electric_car.power_consumption * mileage / 1000 * get_power_price()
        assert res == expected


class TestCalculator:
    def test_add_car(self, calculator, car):
        calculator.add_car(car)
        assert calculator.cars
        assert car in calculator.cars
        assert calculator.cars[car] > 0

    def test_print_cars(self, calculator):
        calculator.print_cars()
    
    def test_get_left_price(self, calculator, car):
        res = calculator.get_left_price(car)
        assert res

class TestApi:
    @pytest.mark.parametrize('function', [get_gas_price, get_power_price])
    def test_get_price(self, function):
        res = function()
        assert isinstance(res, int) or isinstance(res, float)

    @pytest.mark.parametrize('a, b, result', data)
    def test_sum(self, a, b, result):
        # является ли какое-то утверждение верным
        res = add_two_numbers(a, b)
        assert res == result


#Для просмотра покрытия pytest --cov . --cov-report term-missing --cov-fail-under 100 в терминале