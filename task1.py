massiv=[10, 20, 30, 40, 50]
while True:
   def task1(massiv):
      percent=int(input("enter the percentage:"))
      index=0
      while index < len(massiv):
         p=(massiv[index] * percent) // 100
         print(p)
         index+=1


task1(massiv)
