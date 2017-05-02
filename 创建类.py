#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
	'所有员工的基类'
	empcount=0


	def __init__(self,name,salary):
	 self.name=name
	 self.salary=salary
	 Employee.empcount+=1

	def displaycount(self):
	 print "Total Employee %d" %Employee.empcount

	def displayEmployee(self):
	 print "Name :",self.name, ", Salary: ",self.salary


"创建Employee类的第一个对象"
emp1=Employee("zara",2000)
"创建Employee类的第二个对象"
emp2=Employee("manni",5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" %Employee.empcount

emp1.age=7      #添加一个'age'属性
emp1.age=8      #修改'age'属性
#del emp1.age    #删除属性'age'
print"emp1.age是 %d" %emp1.age

hasattr(emp1,'age')     #如果存在'age'属性选择True
getattr(emp1,'age')     #返回'age'的值
setattr(emp1,'age',8)   #添加属性'age'值为8
delattr(emp1,'age')     #删除属性值'age'

#python内置类属性
print"Employee.__doc__:",Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
