fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)

fruits.extend(points)
fruits.index("cherry")

fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

cars = ['Ford', 'BMW', 'Volvo']
cars.reverse()
print(cars)


# A function that returns the length of the value:
def my_func(e):
    return len(e)


cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=my_func)

print(cars)


def my_function(e):
    return e['year']


cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]

cars.sort(key=my_function)

print(cars)
