#NYOMAN ADI ARYA SUABAKTI/2415091013
def cyclic_left_shift(array, n):
    n = n % len(array)
    return array[n:] + array[:n]

array = eval(input())
if not isinstance(array, list) or len(array) == 0:
    print("No proceed")
else:
    k = int(input())
    result = cyclic_left_shift(array, k)
    print(result)