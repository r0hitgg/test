i = int(input('''choose 1 for seprate every character\n 2 for seprate with comma in amount format'''))
if i == 1:
    inp1 = int(input())
    print("number with coma " + "{:,}".format(inp1))
if i == 2:
    inp = input()
    inp = [int(i) for i in inp]
    for i in inp:
        print(i,end=',')
