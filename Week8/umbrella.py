weather = input("What is the weather like today (rainy, sunny, cloundy)?")
temperature = int(input("What is the temperature outside?"))

if weather == 'rainy':
    if temperature  < 60:
        print("You should take an umbrella and a jacket.")
    else:
        print("You should take an umbrella.")
elif weather == 'sunny':
    if temperature > 75:
        print("You should wear sunscreen.")
    else:
        print("You should wear sunglasses.")
elif weather == 'cloudy':
    if temperature  < 60:
        print("You should take an umbrella and a jacket.")
    else:
        print("You should take an umbrella.")
else:
    print("I don't know what that is!")