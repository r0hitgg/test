inp = input()
inp1 = int(input())
print("number with coma " + "{:,}".format(inp1))
inp = [int(i) for i in inp]
for i in inp:
    print(i,end=',')
