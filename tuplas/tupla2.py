nums = (5,4,3,-2,1,6,455,3,6,6,6,6,6)
mayor = nums[0]
menor = nums[0]
 
for i in nums:
    if i > mayor:
        mayor = i
 
    if i < menor:
        menor = i
 
print("El mayor de la lista es: ",mayor)
print("El menor de la lista es: ",menor)