def one():
    number = 12

    for factor in range(2, number + 1):
        if number % factor == 0:
            is_prime = True

            for divisor in range(2, factor):
                if factor % divisor == 0:
                    is_prime = False

            if is_prime:
                print(factor)


def two():
    n = 8

    if n == 1:
        print(0)
        return

    first = 0
    second = 1
    count = 2

    while count <= n:
        next_number = first + second
        first = second
        second = next_number
        count = count + 1

    print(first)


def three():
    word_one = "listen"
    word_two = "silent"

    if len(word_one) != len(word_two):
        print(False)
        return

    for letter in word_one:
        if word_one.count(letter) != word_two.count(letter):
            print(False)
            return

    print(True)


def four():
    n = 10
    start = 2
    difference = 2
    count = 0
    number = start

    while count < n:
        print(number)
        number = number + difference
        count = count + 1


def five():
    numbers = [1, 4, 7, 4, 2, 8, 9, 7, 4]
    
    length = len(numbers)
    for i in range(length):
        for j in range(0, length - i - 1):
            if numbers[j] > numbers[j + 1]:

                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

    if length % 2 == 1:
        middle_index = length // 2
        print(numbers[middle_index])
    else:
        middle_index_1 = length // 2 - 1
        middle_index_2 = length // 2
        median = (numbers[middle_index_1] + numbers[middle_index_2]) / 2
        print(median)


def six(number):
    total = 0
    divisor = 1

    while divisor < number:
        if number % divisor == 0:
            total = total + divisor

        divisor = divisor + 1

    if total == number:
        print(True)
    else:
        print(False)


def seven():
    number = 12345
    text = str(number)
    total = 0

    for digit in text:
        total = total + int(digit)

    print(total)


def eight():
    sentence = "Python programming is interesting"
    words = sentence.split()

    longest = words[0]
    index = 0

    while index < len(words):
        if len(words[index]) > len(longest):
            longest = words[index]

        index = index + 1

    print(longest)


def nine():
    sentence = "The quick brown fox jumps over the lazy dog"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()

    for letter in alphabet:
        if letter not in sentence:
            print(False)
            return

    print(True)


def ten():
    number = 2

    while number <= 1000:
        is_prime = True
        divisor = 2

        while divisor < number:
            if number % divisor == 0:
                is_prime = False

            divisor = divisor + 1

        if is_prime:
            print(number)

        number = number + 1