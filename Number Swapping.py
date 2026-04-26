
name="Sukriti"
age=12
is_student=True
weight=39.5

print("Name:",name)
print("Data Type ofName",type(name))
print("Age :", age)
print("Data Type of Age is",type(age))
print("is_student :", is_student)
print("Weight:",weight)
print("Data Type of weight is",type(weight))

print("\n After Type Casting....")
age=str(age)
print("Data Type of age is",type(age))
weight=int(weight)
print(weight)
print("Data Type of weight is",type(weight))






num1=65
num2=5

print("Number 1",num1)
print("Number 2",num2)
print("Addition :",num1+num2)
print("Difference :",num1-num2)
print("Product :",num1*num2)
print("Division :",num1/num2)
print("Floor Division :",num1//num2)
print("Modules Operation :",num1%num2)
print("Square :",num2**2)
print("Square Root :",num1**8.5)

print("Equal ?", num1==num2)
print("Number 1 greater?",num1>num2)
print("Number 2 greater?",num1<num2)
print("Not Equal ?",num1!=num2)

result = num1/num2+num2**2+10
print("Result of given equation is ",result)










first_name ="Sukriti"
last_name ="Sharma"
full_name = first_name+last_name
example ="Haa"*5

print("First Name :",first_name)
print("Last Name :",last_name)
print("Full Name :", full_name)
print("String Multiplied 5 times given this result :", example)

word = 'Sukriti'
print("Length of String :",len(word))
print("First Letter of String :",word[4])
print("Last Letter of String :",word[5])
print("String Sliced :",word[0:3])









x = input("Enter value of x :")
y =input("Enter value lof y:")
temp  = x
x = y 
y = temp
print("value of x after swapping", x)
print("value of y after swapping", y)