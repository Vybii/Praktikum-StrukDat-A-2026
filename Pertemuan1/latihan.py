n = 15
k = 1

while n > k:
    print(k)
    if k == n + 1:
        break
    k += 1

def fizzbuzz_plus(k):
    print("FizzBuzz") if ((k % 3 == 0) & (k % 5 == 0)) else print("Fizz") if (k % 3 == 0) else print("Buzz") if (k % 5 == 0) else print("Seven") if (k % 7 == 0) else print(k)
       

fizzbuzz_plus(k)