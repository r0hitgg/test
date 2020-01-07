x = input("enter a string")
x = [char for char in x]
for i in range(0,len(x)):
    if(i%2 == 0):
        print(x[i],end='')
    else:
        continue
print('hello')
