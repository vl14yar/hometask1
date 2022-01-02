x = 8
y = 2
print(x+y)
print(f'Sum {x} + {y} = {x+y}')
print(f'Віднімання {x} - {y} = {x-y}')
print(f'Ділення {x} / {y} = {x/y}')
print(f'Множення {x} * {y} = {x*y}')
print(type(x/y))
result = int(x/y)
print(result)
print(f'Степінь {x} ** {y} = {x**y}')
z = 9
r = 2
print(f'Цілочисельне {z} // {r} = {z//r}')
print(f'Модело {z} % {r} = {z%r}')
float_number = 3.8762742596
print(round(float_number, 2))
print('1'+'2')
print(4* '2')
print(9 ** 1/2)

new_line = 'We all live in a yellow submarine\nYellow submarine, yellow submarine\nWe all live in a yellow submarine\nYellow submarine, yellow submarine'
tripple_quotes1 = """We all live in a yellow submarine
Yellow submarine, yellow submarine
We all live in a yellow submarine 
Yellow submarine, yellow submarine"""
triple_quotes = """#########
#     #
#     #
#     #
#########

#     #
#     #
#########
#     #
#     #"""
print(new_line)
print(triple_quotes)
print(tripple_quotes1)
start_string = "abcdefghijklmn"
new_string_first = start_string[0:5]
print(new_string_first)
new_string_reverse = start_string[8:13]
print(new_string_reverse)
every_second = start_string[::2]
print(every_second)
new_string_mid = start_string[5:9]
print(new_string_mid)
pattern = 'Pattern.text: {surname}, {name}'
print(pattern.format(surname='Заборський', name='Володимир'))
txt = "hello, world."
i = txt.capitalize()
print (i)

txt = "Hello, World!"
a = txt.casefold()
print(a)

txt = "grape"
o = txt.center(15)
print(o)

txt = "I love Python, Python is my favourite codding language"
x = txt.count("Python")
print(x)

txt = "My name is Ståle"
x = txt.encode()
print(x)

txt = "Hello, world."
x = txt.endswith(".")
print(x)

txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)

txt = "Hello, world."
x = txt.find("Hello")
print(x)

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 1000))
txt = "Ukrainian is my favourite language"
x = txt.index("favourite")
print(x)

txt = "Player3858"
x = txt.isalnum()
print(x)

txt = "Player3858"
x = txt.isalpha()
print(x)

txt = "Player3858"
x = txt.isascii()
print(x)

txt = "\u0033" '#unicode for 3'
x = txt.isdecimal()
print(x)

txt = "5385243496"
x = txt.isdigit()
print(x)

txt = "Mode"
x = txt.isidentifier()
print(x)

txt = "Hello world!"
x = txt.islower()
print(x)

txt = "13057306723475910"
x = txt.isnumeric()
print(x)

txt = "Hello! Are you Player3858?"
x = txt.isprintable()
print(x)

txt = "        "
x = txt.isspace()
print(x)

txt = "Hello, World!"
x = txt.istitle()
print(x)

txt = "JUST DO IT!"
x = txt.isupper()
print(x)

myTuple = ("Viktor", "Vladimir", "Ivan")
x = "#".join(myTuple)
print(x)

txt = "Ukrainian"
x = txt.ljust(10)
print(x, "is my favorite language.")

txt = "Hello WORLD"
x = txt.lower()
print(x)

txt = "     Ukrainian     "
x = txt.lstrip()
print("Of all Languages", x, "is my favorite")

txt = "Hello Ram!"
mytable = txt.maketrans("a", "e")
print(txt.translate(mytable))

txt = "I could eat apples all day"
x = txt.partition("apples")
print(x)

txt = "I like boxing"
x = txt.replace("boxing", "basketball")
print(x)

txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

txt = "Apple"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

txt = "I could eat apples all day, apples are my favorite fruit"
x = txt.rpartition("apples")
print(x)

txt = "apple, grape, cherry"
x = txt.rsplit(", ")
print(x)

txt = "     apple     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

txt = "welcome to the Motherland"
x = txt.split()
print(x)

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

txt = "Hello, world."
x = txt.startswith("Hello")
print(x)

txt = "     apple     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

txt = "Hello My Name Is VOVA"
x = txt.swapcase()
print(x)

txt = "Welcome to the Ukraine"
x = txt.title()
print(x)

mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

txt = "Hello, world"
x = txt.upper()
print(x)

txt = "50"
x = txt.zfill(10)
print(x)
