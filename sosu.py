numbers = "17"
numbers2 = list(numbers)
numbers2.sort()


def isPrime(num):
    for i in range(2,num):
        if num % i ==0 :
            return False

