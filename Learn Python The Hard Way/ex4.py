#! python3


cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print('There are', str(cars), 'cars available.')
print('There are only', str(drivers), 'drivers available.')
print('There will be', str(cars_not_driven), 'empty cars today.')
print('We can transport' , str(int(carpool_capacity)), 'people today.')
print('We have', str(passengers), 'to carpool today.')
print('We need to put about', str(int(average_passengers_per_car)),
     'in each car.')

