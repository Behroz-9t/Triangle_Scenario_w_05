# 🧮 Week 05 OOP Assignment – Triangle Scenario in Python

This project demonstrates the use of Object-Oriented Programming (OOP) concepts in Python by modeling a geometric Triangle with various constructors, encapsulated properties, validation, object cloning, static members, and basic geometric logic.

## 🚀 Features

- ✅ Custom Triangle class with flexible constructors
- 🔁 Constructor overloading handled Pythonically
- 📏 Side validation using `@property` decorators
- 📐 Methods to calculate perimeter and detect right-angled triangles
- 🧬 Object cloning using an existing triangle instance
- 📊 Class method to track number of Triangle objects created
- 🔍 Clean string representation with `__str__`

## 🧱 Class Overview

```python
class Triangle:
    def __init__(self, x=1.0, y=None, z=None, existing_triangle=None):
        ...
```

- If no arguments: creates an equilateral triangle with sides = 1.0  
- If one argument: creates an equilateral triangle with given side  
- If two arguments: creates an isosceles triangle (x, x, y)  
- If three arguments: creates a triangle with sides (x, y, z)  
- If `existing_triangle` is passed: creates a deep copy of the triangle  

## 🔒 Property Validation

Each side uses the `@property` and setter decorators to ensure that:

- Side values are always positive
- Logic is encapsulated cleanly
- Access looks like regular attributes but safely invokes validation logic

## 🔁 Static & Instance Methods

- `Triangle.objectCount()`: returns number of triangle instances created  
- `triangle.perimeter()`: returns perimeter of the triangle  
- `triangle.is_right_angled()`: checks if triangle follows the Pythagorean theorem  

## 🧪 Example Usage

```python
t1 = Triangle(3, 4, 5)
print(t1.perimeter())              # 12
print(t1.is_right_angled())        # True

t2 = Triangle(existing_triangle=t1)
print(t2)                          # Triangle with sides (3, 4, 5)
print(Triangle.objectCount())      # 2
```

## 🎯 OOP Concepts Practiced

- Class and instance attributes  
- Constructor overloading  
- Encapsulation and validation via `@property`  
- Static/class methods  
- Object cloning  
- Geometric logic (Pythagoras + perimeter)

## 📂 Structure


Triangle_class
        Class.py     

main.py

Uml
    UML_Triangle.png

README.md
