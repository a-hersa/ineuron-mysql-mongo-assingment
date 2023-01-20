# q1 : Create your own class to perform a list search operation
class ListSearch:
    def __init__(self, lst):
        self.lst = lst

    def search(self, n):
        for i in range(len(self.lst)):
            if self.lst[i] == n:
                return True
        return False

lst = [1, 2, 3, 4, 5]
search = ListSearch(lst)
print("q1")
print(search.search(3)) # True
print(search.search(6)) # False

# q2 : create a class for dict new element addition
class DicAdd:
    def __init__(self, dic):
        self.dic = dic
    
    def add(self, k, v):
        self.dic[k] = v

dic = {
    "brand" : "opel",
    "model" : "corsa"
}
cars = DicAdd(dic)
cars.add("year", 2005)
print("q2")
print(dic)

# q3 : create a class for tuple data extraction operation
class TupleExtractor:
    def __init__(self, tup):
        self.tup = tup

    def extract(self, index):
        try:
            return self.tup[index]
        except IndexError:
            return None

tup = (1, 2, 3, 4, 5)
extractor = TupleExtractor(tup)
print("q3")
print(extractor.extract(3)) # 4
print(extractor.extract(10)) # None

#q4 : Create a class to implement all insert , update , delete operation for mysql
import mysql.connector

class sql:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="",
            user="",
            password="",
            database=""
        )
        self.mycursor = self.mydb.cursor()
    
    # Insert a lists where every element is an entry
    def sqlInsert(self, table, *args):
        for course in args:
            sql = "INSERT INTO "+ table + "(CourseName, Instructor, CourseUrl) VALUES (%s, %s, %s)"
            val = (course[0], course[1], course[2])
            self.mycursor.execute(sql, val)
            self.mydb.commit()
        print(len(args), "record(s) inserted in mysql.")
    
    # Update val1 with val2 in column
    def sqlUpdate(self, table, column, oldVal, newVal):
        sql = "UPDATE "+ table +" SET " + column + " = %s WHERE " + column + " = %s"
        val = (newVal, oldVal)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "record(s) updated in mysql.")

    # Delete val from column
    def sqlDelete(self, table, column, val):
        sql = "DELETE FROM "+ table +" WHERE " + column + " = %s"
        val = (val, )
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "record(s) deleted in mysql.")

ineurondb = sql()
#ineurondb.mycursor.execute("CREATE TABLE courses(CourseName varchar(255),Instructor varchar(255),CourseUrl varchar(255))")
ineurondb.sqlInsert("Courses",
    ["Complete Excel Course", "Dr. Nishtha Jain", "https://ineuron.ai/course/Complete-Excel-Course"],
    ["Complete DSA in Python", "Priya Bathia", "https://ineuron.ai/course/Complete-DSA-in-Python"],
    ["Tableau Foundation Course", "Dr. Nishtha Jain", "https://ineuron.ai/course/Tableau-Foundation-Course"]
)

ineurondb.sqlUpdate("Courses", "Instructor", "Dr. Nishtha Jain", "Krish Naik")
ineurondb.sqlDelete("Courses", "Instructor", "Krish Naik")

#q5 : create a class to implement insert , update and delete in monngo db

import pymongo

class mongo:
    def __init__(self):
        self.client = pymongo.MongoClient("")
        self.db = self.client.test
        self.database = self.client['']
        self.coll = self.database['']
    
    # pass each course as a list with course name, instructor and course URL
    def mongoInsert(self, *args):
        many_data = []
        for course in args:
            many_data.append({
                "CourseName":course[0],
                "Instructor":course[1],
                "CourseUrl":course[2]
                })
        self.coll.insert_many(many_data)
        print(len(many_data), "record(s) inserted in mongodb.")
    
    # update all records defining the field to update, the old value to replace and the new value
    def mongoUpdate(self, field, oldVal, newVal):
        myquery = { field: oldVal }
        newvalues = { "$set": { field: newVal } }
        x = self.coll.update_many(myquery, newvalues)
        print(x.modified_count, "record(s) updated in mongodb.") 

    # delete all fields that contain value
    def mongoDelete(self, field, val):
        myquery = { field: val}
        x = self.coll.delete_many(myquery)
        print(x.deleted_count, "record(s) deleted in mongodb.") 

ineuronmongo = mongo()
ineuronmongo.mongoInsert(
    ["Complete Excel Course", "Dr. Nishtha Jain", "https://ineuron.ai/course/Complete-Excel-Course"],
    ["Complete DSA in Python", "Priya Bathia", "https://ineuron.ai/course/Complete-DSA-in-Python"],
    ["Tableau Foundation Course", "Dr. Nishtha Jain", "https://ineuron.ai/course/Tableau-Foundation-Course"]
)

ineuronmongo.mongoUpdate("Instructor", "Dr. Nishtha Jain", "Krish Naik")
ineuronmongo.mongoDelete("Instructor", "Krish Naik")

#q6 : create a class to perform append and delete operation in a file and inherit it in child class

class doc():
    def __init__(self, doc):
        self.doc = doc

    #append string as a new line in a file
    def append(self, data):
        with open(self.doc, "a") as doc:
            data = doc.write("\n"+data)
        print("text appended.")

    #delete all text from file
    def delete(self):
        with open(self.doc,'w') as doc:
            pass

doc = doc("file.txt")
doc.append("test")
doc.delete()

#q7 : create a class to import a data into file from mongo db

class export(mongo):

    # export all data from a collection into a file
    def toFile(self, file):
        with open(file, "a") as doc:
            for entry in self.coll.find():
                for x, y in list(entry.items())[1:]:
                    #for x, y in dic.items():
                    data = doc.write(str(x)+":"+str(y)+"\n")
                data = doc.write("\n")

                #data = doc.write(x+"\n")
                #data = doc.write("\n" + self.db.random.find({}))
        print("mongo collection exported successfully.")

export = export()
export.toFile("mongo.txt")


#q8 : Create a class to build a calculator funcnalities addition , subtraction , multiplication ,div , log , exponenet , power

import math

class calculator():

    def add(self, *args):
        return sum(args)

    def subtract(self, *args):
        result = args[0]
        print(result)
        for num in args[1:]:
            result -= num
        return result

    def multiply(self, *args):
        result = args[0]
        print(result)
        for num in args[1:]:
            result = result * num
        return result
    
    def division(self, *args):
        result = args[0]
        print(result)
        for num in args[1:]:
            result = result / num
        return result

    def log(self, num, base):
        return math.log(num, base)

    def exp(self, num):
        return math.exp(num)
    
    def pow(self, base, exp, mod):
        return pow(base, exp, mod)

calc = calculator()
print(calc.add(2, 3, 4, 5))
print(calc.subtract(10, 3, 2))
print(calc.multiply(10, 3, 2))
print(calc.division(60, 3, 2))
print(calc.log(9, 3))
print(calc.exp(65))
print(calc.pow(4, 3, 5))

# q9 : create a class method to find a time and space complexity of any function
import time
import tracemalloc

class ComplexityAnalyzer:
    def analyze(self, func):
        def wrapper(*args, **kwargs):
            tracemalloc.start()
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            print("Time complexity: O({:.6f})".format((end_time - start_time)))
            print("Space complexity: {} bytes".format(peak))
            return result
        return wrapper


analyzer = ComplexityAnalyzer()

@analyzer.analyze
def multiply(*args):
    result = args[0]
    print(result)
    for num in args[1:]:
        result = result * num
    return result
    
print(multiply(2, 5, 3))

# q10: create a class to do a bulk uplaod of a file in mysql
import pandas as pd
import numpy as np

class csv(sql):
    def __init__(self, file):
        self.file = file

    def csvimport(self):
        empdata = pd.read_csv(self.file, index_col=False, delimiter=",", header=None).fillna(0)
        for i, row in empdata.iterrows():
            sql = """INSERT INTO clients(
                                    ClientName,
                                    ClientSurname,
                                    Street,
                                    City,
                                    State,
                                    Zipcode
                                    ) VALUES (%s, %s, %s, %s, %s, %s)"""
            ineurondb.mycursor.execute(sql, tuple(row))
            print("record inserted.")
            ineurondb.mydb.commit()

clientscsv = csv("clientsCSV.csv")
#clientscsv.mycursor.execute("""CREATE TABLE clients(
#                                    ClientName varchar(255),
#                                    ClientSurname varchar(255),
#                                    Street varchar(255),
#                                    City varchar(255),
#                                   State varchar(255),
#                                    Zipcode varchar(255))""")
clientscsv.csvimport()

# q11: give 10 different example of ploymorphism , encaptulation ,data  abstraction , overloading , ovverriding , multiple inheritance

#Polymorphism:
def print_data(data):
    print(data)

print_data(1) # prints 1
print_data("hello") # prints hello
print_data([1,2,3]) # prints [1,2,3]

#Encapsulation:
class MyClass:
    def __init__(self):
        self.__private_var = 0

    def set_private_var(self, value):
        self.__private_var = value

    def get_private_var(self):
        return self.__private_var

obj = MyClass()
obj.set_private_var(10)
print(obj.get_private_var()) # prints 10

#Abstraction:
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(2, 3)
print(rect.area()) # prints 6

#Overloading:
class MyClass:
    def my_method(self, a):
        print(a)

    def my_method(self, a, b):
        print(a + b)

obj = MyClass()
obj.my_method(1) # this will throw an error
obj.my_method(1, 2) # prints 3

#Overriding:
class Parent:
    def my_method(self):
        print("Parent method")

class Child(Parent):
    def my_method(self):
        print("Child method")

obj = Child()
obj.my_method() # prints "Child method"

#Multiple Inheritance:
class Parent1:
    def my_method(self):
        print("Parent1 method")

class Parent2:
    def my_method(self):
        print("Parent2 method")

class Child(Parent1, Parent2):
    pass

obj = Child()
obj.my_method() # prints "Parent1 method"

#Operator overloading:
class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyNumber(self.value + other.value)

num1 = MyNumber(1)
num2 = MyNumber(2)
result = num1 + num2
print(result.value) # prints 3

#Property decorator for encapsulation:
class MyClass:
    def __init__(self):
        self.__x = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

obj = MyClass()
obj.x = 10
print(obj.x) # prints

#q12: Try to explore a meaning of "-> " this sinnature in python 
"""The "-> " notation in Python is used to indicate the return type of a function or method.
It is used in type hints and type annotations, which are a way to specify the types of variables,
function arguments and return values in Python.

In Python 3.5 and later versions, the "-> " notation can be used in function annotations,
which are a way to provide type hints for functions. The notation is used to indicate the return type of a function. For example:"""

def add(a: int, b: int) -> int:
    return a + b




