first = input("enter first number : ");
first = int(first);
operator = input("enter opearation (+, -, %, /, *) : ");
second = input("enter second number : ");
second = int(second);

if(operator == "+"):
    print(first+second);

elif(operator == "-"):
    print(first-second);

elif(operator == "*"):
    print(first*second);

elif(operator == "/"):
    print(first/second);

elif(operator == "%"):
    print(first%second);

else:
    print("invalid operation");