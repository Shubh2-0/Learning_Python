try:
    f = int(input("Enter your age : "))
    if(f<=0):
        print("Age is lees than 1")
    else:
        print("Hello your age is :"+str(f))
except:
    print("Invalid age")
