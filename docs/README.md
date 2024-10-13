
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# General description of the solution
The library is designed to simplify and automate the calculation of the perimeter and area of geometric shapes: *circle*, *square* and *triangle*.
To accomplish these tasks, Python functions were created that calculate the perimeter and area of the named shapes. Each shape has its own function.

# Description of each function with call examples
## triangle
```python
def area(a, b, c):
    '''Функция принимает значения - стороны треугольника'''
    return (a + b + c) / 2
    '''Функция возвращает (a + b + c) / 2'''

def perimeter(a, b, c):
    '''Функция принимает значения - стороны треугольника'''
    return a + b + c
    '''Функция возвращает периметр треугольника'''
```

## Example of function input

```python
print(area(1, 2, 3))
print(perimeter(1, 2, 3))
```

## Example of function output

```python
3.0
6
```

## square
```python
def area(a):
    '''Принимает число n - сторона квадрата'''
    return a * a
    '''Возвращает площадь квадрата'''

def perimeter(a):
    '''Принимает число n - сторона квадрата'''
    return 4 * a
    '''Возвращает периметр квадрата'''
```

## Example of function input

```python
print(area(4))
print(perimeter(4))
```

## Example of function output

```python
16
16
```

## circle
```python
import math


def area(r):
    '''Функция принимает значение - радиус круга'''
    return math.pi * r * r
    '''Функция возвращает площадь круга'''


def perimeter(r):
    '''Функция принимает значение - радиус круга'''
    return 2 * math.pi * r
    '''Функция возвращает периметр круга'''
```

## Example of function input

```python
print(area(8))
print(perimeter(8))
```

## Example of function output

```python
201.06192982974676
50.26548245743669
```

## calculate
```python
import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)
```

# Commits with hashes
## L-03
- 8ba9aeb: Circle and square added
- d078c8d: Docs added
- 6adb962: Docs added

## L-04
- d080c78: Triangle added
- 51c40eb: Doc updated for triangle
- d76db2a: Add calculate.py
- b5b0fae: Update docs for calculate.py
- 3049431: Add rectangle.py

## L-05
- 438b89a: Add user agreement
- 86edb1c: Update Docs. Add user agreement info

