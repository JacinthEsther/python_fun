def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year{year}: ${amount:,.2f}")


amount = float(input("Enter a principal amount: "))
rate = float(input("Enter an annual rate of return: "))
years = int(input("Enter a number of years: "))

invest(amount, rate, years)


# LEGB: Local,Enclosing,Global,Built-in


def get_word(word):
    if len(word) < 5:
        print("Your input is less than 5 characters long.")
    elif len(word) > 5:
        print("Your input is greater than 5 characters long.")
    else:
        print("Your input is 5 characters long.")


word = input("enter a word: ")
get_word(word)
