#QUESTION
#Write a small program to explain if-else statements. Elaborate it by giving input and explain the output.

#SOLUTION:
#Just to explain if-else statement, i am going to make a simple calculator using if-then statements.

num_1 = float(input("ENTER FIRST NUMBER: "))
operator = input("ENTER THE OPERATOR: ")
num_2 = float(input("ENTER ANOTHER NUMBER: "))

if operator == '+':
    print(num_1 + num_2) 
elif operator == '-':
    print(num_1 - num_2)
elif operator == '*':
    print(num_1 * num_2)
elif operator == '**':
    print(num_1 ** num_2)
else:
    print(num_1 / num_2)

#Here we have mentioned the various arithematic operators using if-else and elif statement. When we enter both the number and operator, the compiler runs through the program and finds the suitable operation for the command and then executes it.   
            


