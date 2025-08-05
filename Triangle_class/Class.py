import math #--> Python in-built module
class Triangle:
    

    object_count = 0 #--> Class variable declaration and initialization for obj counting.

    def __init__(self,x=1.0,y=None,z=None,existing_triangle=None):
        
    #Checks if existing triangle value is given 
        if existing_triangle:

            self.sideA=existing_triangle.sideA
            self.sideB=existing_triangle.sideB
            self.sideC=existing_triangle.sideC

    #For Equilateral_triangle
        elif y is None and z is None :
            self.sideA=self.sideB=self.sideC=x
            print(f"Created the Equilateral triangle of sides A: {self.sideA} , side B: {self.sideB} and side C: {self.sideC}")

    #For Isosceles_triangle
        elif z is None:
            self.sideA=self.sideB=x
            self.sideC=y
            print(f"Created the Isosceles triangle of side A: {self.sideA} , side B: {self.sideB} and side C: {self.sideC}")
        

    #For Scalene_triangle
        else:
            self.sideA=x
            self.sideB=y
            self.sideC=z
            print(f"Created the Scalene triangle of side A: {self.sideA} , side B: {self.sideB} and side C: {self.sideC}")


        Triangle.object_count+=1 #--> Accessing the class variable in constructor with class reference(Triangle).



    @property  #--> Getter Method for side A which treats method like attributes
    def sideA(self):
        return self._a

    @sideA.setter #--> Setter Method which is invoked when attribute is sett in main (assignment operation)
    def sideA(self,value):
        if value > 0:
            self._a=value
        else:
            raise ValueError("Side A must be greater than 0") #The check for suitable side value
    
    

    @property  #--> Getter Method for side B
    def sideB(self):
        return self._b
    
    @sideB.setter #--> Setter Method  
    def sideB(self,value):
        if value > 0:
            self._b=value
        else:
            raise ValueError("Side B must be greater than 0")


    
    @property  #--> Getter Method for side C
    def sideC(self):
        return self._c
    
    @sideC.setter #--> Setter Method 
    def sideC(self,value):
        if value > 0:
            self._c=value
        else:
            raise ValueError("Side C must be greater than 0") 
        



    @classmethod #--> Decorator for accessing of class method via (cls) reference
    def objectCount(cls):
       return Triangle.object_count 

    
    

    def perimeter(self): #--> For the perimeter of the triangle
       return self.sideA+self.sideB+self.sideC
    

    
    def is_it_right_angled(self):#--> To check whether the triangle is right angled or not

        a,b,c=sorted([self.sideA,self.sideB,self.sideC]) #--> sorted values in this way "a" is always the smallest side
        #than "b" and then "c" will be the longest side which will be our hypotenuse. We did this to implement the 
        #pythagoras theorem to check the right-angled triangle 
    
        return math.isclose(a**2+b**2,c**2) #--> here math is the module and .isclose is its method. We use .isclose for 
        #betterprecision and handling of floating-point rounding issues. And in the parenthesis we implemented pythagoras theorem.

    
    
    def __str__(self):#--> __str__ is the magic dunder method of pyhton which controls what should be returned when the class object is represented as a string and printed.
        return f"The triangle consists of side A: {self.sideA} , side B: {self.sideB} and side C: {self.sideC}."


