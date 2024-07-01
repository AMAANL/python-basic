print('Day 2: 30 Days of python programming')
first_name='Amaan'
last_name='Lakdawala'
full_name='Amaan'+ ' Lakdawala'
country='India'
city='Mumbai'
age=19
year=2024
is_married='false'
print(first_name, last_name, country, age, is_married)

print(len( first_name ))  

challenge = 'thirty days of python'
print(challenge.capitalize()) 
print('In every programming language it starts with \"Hello, World!\"')

challenge = 'thirty days of python'
print(challenge.count('y')) 
print(challenge.count('y', 7, 14)) 
print(challenge.count('th')) 

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.rstrip(" "))

# insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango