import calculator


if __name__ == '__main__':
    calc = calculator.Calculator(years=3)
    calc.add_car(
        calculator.Car('Toyota Corolla', price=120000, fuel_economy=7, service_cost=1200, insurance_cost=2500)
    )
    calc.add_car(
        calculator.ElectricCar('Tesla Model 3', 200000, 5500, 150)
    )
    calc.add_car(
        calculator.Car('Range Rover', 650000, 3, service_cost=3000, insurance_cost=7000)
    )

    calc.print_cars()