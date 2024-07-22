def swap(list):
    Num=len(list)

    Num1=list[0]
    list[0]=list[Num-1]
    list[Num-1]=Num1

    return list
i=[12,35,9,56,24]
print(i)
print("Swapping :",swap(i))