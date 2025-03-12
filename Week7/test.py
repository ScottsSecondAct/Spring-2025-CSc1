
def power(base, exponent):
    print("Yeah")
    if (base == 2):
        print("base=2")
    return base ** exponent

def odd_even(number):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

def format_title(title):
    words = title.split()
    capitalized_words = [word.capitalize() for word in words] 
    capitalized_text = " ".join(capitalized_words)
    return capitalized_text

# number = 2 => number % 2 = 0
# number = 3 => number % 2 = 1

num = power(2,5)
print(num)
num = odd_even(num)
print(num)

print("10%")

str = format_title("hello scott")
print(str)