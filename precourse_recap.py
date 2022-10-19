name = "Chris"
age = 36 
daughter = "Poppy"
working = 21

hello_statement = "Hello my name is " + name.lower() + " and I am " + str(age) + " years old."

working_life = age - working

working_life_statement = "I've been working now for around " + str(working_life) + " years as a software tester"


full_message = hello_statement + " " + working_life_statement

print(full_message)