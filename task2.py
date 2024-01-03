list = [1, 2, 3, 3, 2, 1, 6, -1, 5, 6, 5]

def search(massiv1):
   result = 0
   for num in massiv1:
      result ^= num
   return result


search(massiv1=list,)