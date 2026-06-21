def one():
    numbers = [1, 4, 7, 4, 2, 8, 9, 7, 4]
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    print(largest)


def two():
    numbers = [1, 4, 7, 4, 2, 8, 9, 7, 4]
    total = 0
    index = 0

    while index < len(numbers):
        total = total + numbers[index]
        index = index + 1

    average = total / len(numbers)
    print(average)


def three():
    text = "radar"
    reversed_text = ""

    for letter in text:
        reversed_text = letter + reversed_text

    if text == reversed_text:
        print(True)
    else:
        print(False)


def four():
    n = 10
    number = 2
    count = 0

    while count < n:
        print(number)
        number = number * 2
        count = count + 1


def five():
    numbers = [1, 4, 7, 4, 2, 8, 9, 7, 4]
    largest = numbers[0]
    second_largest = numbers[0]

    for number in numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number

    print(second_largest)


def six(number):
    factorial = 1
    i = 1

    while i <= number:
        factorial = factorial * i
        i = i + 1

    print(factorial)


def seven():
    number = 81
    i = 1

    while i * i < number:
        i = i + 1

    if i * i == number:
        print(True)
    else:
        print(False)


def eight(limit):
    total = 0

    for number in range(2, limit + 1):
        is_prime = True

        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False

        if is_prime:
            total = total + number

    print(total)


def nine():
    sentence = "Hello, world! This is Python."
    sentence = sentence.replace(",", " ")
    sentence = sentence.replace(".", " ")
    sentence = sentence.replace("!", " ")
    sentence = sentence.replace("?", " ")

    words = sentence.split()
    count = 0

    for word in words:
        count = count + 1

    print(count)


def ten():
    list_one = [1, 4, 7, 4, 2, 8, 9, 7, 4]
    list_two = [3, 4, 5, 6, 7]

    index = 0

    while index < len(list_one):
        if list_one[index] in list_two:
            print(list_one[index])

        index = index + 1