

intro = "My name is Shubham Bhati. I am from Ujjain(M.P)"

with open("intro.txt","w") as h:
    h.write(intro)


with open("intro.txt","r") as j:
     g = j.read()
     print(g) 