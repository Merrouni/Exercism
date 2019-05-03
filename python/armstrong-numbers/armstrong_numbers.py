def is_armstrong(number):
    size = len(str(number))
    sum = 0
    for i in str(number):
        sum += pow(int(i), size)
    return sum == number
