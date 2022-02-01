def high_and_low(numbers):
    numbers = numbers.split()
    maxi=mini=int(numbers[0])
    for i in numbers:
        if int(i)>maxi:
            maxi=int(i)
        elif mini>int(i):
            mini=int(i)
    return "{} {}".format(maxi,mini)
