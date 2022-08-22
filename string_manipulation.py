# prompt = input("what is your name? ")
#
# print(prompt.lstrip().upper())
# print(prompt[0:3])

# String interpolation
name = "Girl"
heads = 2
arms = 2
print(name + " has " + str(heads) + " heads and " + str(arms) + " arms")
print(name, "has", str(heads), "heads and", str(arms), "arms")
f"{name} has {heads} heads and {arms} arms"


for n in range(3):
    password = input("Password: ")
    if password == "I<3Bieber":
        break
        # print("Password is incorrect.")
    else:
        print("Suspicious activity. The authorities have been alerted.")