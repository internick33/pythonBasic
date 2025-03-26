tabla = int(input('Que tabla quieres ver? :'))
nums = range(0,11)

for num in nums:
    result = tabla * num
    print(f'{tabla} x {num} = {result}')