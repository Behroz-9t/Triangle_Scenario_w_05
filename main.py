from Triangle_class.Class import Triangle #--> imported Triangle class from folder Triangle_class and file Class.

print("---------------------------------------------")

Tri = Triangle(2) #--> Object created by instantiation
print("The perimeter of the triangle will be: ",Tri.perimeter())#--> prints the perimeter when the method returns value.
print(Tri.is_it_right_angled())
print(Tri) #--> Here __str__ method is being called 

print("---------------------------------------------")

Tri_1 = Triangle(2,3)
print("The perimeter of the triangle will be: ",Tri_1.perimeter())
print(Tri_1.is_it_right_angled())
print(Tri_1)

print("---------------------------------------------")

Tri_2 = Triangle(4,3,5)
print("The perimeter of the triangle will be: ",Tri_2.perimeter())
print(Tri_2.is_it_right_angled())
print(Tri_2)

print("---------------------------------------------")

#Cloning of Tri_2 by passing the argument existing_triangle

Tri_2_clone=Triangle(existing_triangle=Tri_2)
print("The perimeter of the triangle will be: ",Tri_2_clone.perimeter())
print(Tri_2_clone.is_it_right_angled())
print(Tri_2_clone)

print("---------------------------------------------")

print("The total number of triangle objects created: ",Triangle.objectCount()) #--> Prints the total count of the triangle objects created.

print("---------------------------------------------")

Tri_2 = Triangle(-4,3,5) #--> Throws value error because side A has negative value.




