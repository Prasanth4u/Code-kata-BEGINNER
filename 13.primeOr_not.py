fp=int(input(""))
if fp > 1:
    for i in range(2, fp):
        if (fp % i) == 0:
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
