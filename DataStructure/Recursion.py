def recursion(num):
    if num<=0:
        print("Done!")
    else:
        print(num)
        recursion(num-1)

recursion(9)