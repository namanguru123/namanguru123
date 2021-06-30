def reverse(x):  # define a function reverse with variable x
    rev = 0  # take a variable with value 0
    while x > 0:  # start a loop for x>0
        rev = (rev*10) + x % 10   # here rev = rev*10 and + x%10 so if any number is divided by 10 its reminder is last digit which is multiplied by 10 and stored in variable
        x = x//10  # here the inputted number is double divide so the decimal number get cancelled
    print("Reverse of the number = ", rev)  # print the number
a = int(input("Enter Any Number = "))  # it takes the input from user
reverse(a)  # to call the function with value which is the inputted number
