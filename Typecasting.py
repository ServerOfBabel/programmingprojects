#Typecasting
#<class 'str'>
#<class 'int'>
#<class 'float'>
#<class 'bool'>

name = "Biden"
age = 25
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
print(type(age))

name = bool(name)
print(name)