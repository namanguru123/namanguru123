def prime(x):
    for i in range(2,x):
        if x%i == 0:
            print("It is a Composite Number")
            break
    else:
        print("It is a Prime Number")
a=int(input("Enter Any Number = "))
prime(a)