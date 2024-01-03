#task_3
number = (int(input("Sonni kiriting : "))
l = [10,7,4,9,2]
def append(numb,lst):
    for num in lst:
        if num == numb:
            list.remove(num)
            list.append(num)
            print(lst)

        else:
            print("Bu son yo'q")


append(numb=number,lst=list)