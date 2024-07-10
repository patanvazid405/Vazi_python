#functions 
 
def sum(a,b):
    return(a+b)
total=sum(122,13)
print(total)

#keyword arguments

def person(name,age):
    print("name",name)
    print("age",age)

person(age=20,name="vazid")

# def greet(naam,greeting="Hi"):
#     return naam+ ","+" "
# greet1=greet("vazid")

# greet(greet1)

#global scope
hi ="jagan mawayya" 

def hello():
    print(hi)
    str="hello"
hello()    
print(str)


