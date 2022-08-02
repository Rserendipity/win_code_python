complex_one = 1 + 2j
complex_two = 2j
print(complex_one.real)
print(complex_one.imag)
print(complex_two.real)
print(complex_two.imag)

arr = [x for x in range(1, 101, 1) if x % 7 == 0 or (x > 10 and int(x / 10) == 7) or (x % 10 == 7)]
print(arr)
