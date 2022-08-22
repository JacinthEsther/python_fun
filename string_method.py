print("FRIday".casefold())
# casefold() converts string into lower case
print("caseFold".capitalize())
# capitalize converts first character to upper case
print("aunty".center(12))
print("aunty".center(12,"e"))
# The center() method will center align the string,
# using a specified character (space is default) as the fill character.

print("I love apples, apple are my favorite fruit".count("a"))
print("I love apples, apple are my favorite fruit".count("a",10,24))
print("I love apples, apple are my favorite fruit".count("a",10))


txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
print(txt.encode())

txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)
print(x)
x = txt.endswith("my world.")

print(x)



txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


txt = "Hello, welcome to my world."

print(txt.find("q"))
# print(txt.index("q"))


myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)


txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))


txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))


txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(txt.maketrans(x, y, z))
# The maketrans() method itself returns a dictionary describing
# each replacement, in unicode:


txt = "I could eat bananas all day"

x = txt.partition("apples")

print(x)

txt = "Welcome to my world"

x = txt.title()

print(x)

txt = "hello b2b2b2 and 3g3g3g"

x = txt.title()

print(x)

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))