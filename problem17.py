def number_of_letters(n):
    def get_word(n):
        ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        if n < 20:
            return ones[n]
        elif n < 100:
            return tens[n // 10] + ones[n % 10]
        elif n < 1000:
            if n % 100 == 0:
                return ones[n // 100] + "hundred"
            else:
                return ones[n // 100] + "hundredand" + get_word(n % 100)
        elif n == 1000:
            return "onethousand"
    count = 0
    for i in range(1, n+1):
        count += len(get_word(i))
    return count

# example usage
print(number_of_letters(1000)) # expect 21124
