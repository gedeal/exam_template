# My private testings

# https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
# https://jakob-bagterp.github.io/colorist-for-python/ansi-escape-codes/standard-16-colors/#foreground-text-and-background-colors

# Print Color Text using ANSI Code in Python
# The most common way to print colored text is by printing ANSI escape sequences directly. This can be delivered in different formats such as:
#
# Example 1: Build Functions to call
#
# We can build functions to call particular color named functions to execute the relevant ANSI Escape Sequence.
# The below is Python program to print colored text and background

def prRed(skk):         print("\033[91m {}\033[00m".format(skk))
def prGreen(skk):       print("\033[92m {}\033[00m".format(skk))
def prYellow(skk):      print("\033[93m {}\033[00m".format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m".format(skk))
def prPurple(skk):      print("\033[95m {}\033[00m".format(skk))
def prCyan(skk):        print("\033[96m {}\033[00m".format(skk))

def prLightGray(skk):   print("\033[97m {}\033[00m".format(skk))
def prBlack(skk):       print("\033[98m {}\033[00m".format(skk))

prCyan("Hello World, ")
prYellow("It's")
prGreen("Geeks")
prRed("For")
prGreen("Geeks")

print("This is \x1b[31m 31 \x1b[0m text")
print("This is \x1b[32m 32 \x1b[0m text")
print("This is \x1b[33m 33 \x1b[0m text")
print("This is \x1b[34m 34 \x1b[0m text")
print("This is \x1b[35m 35 \x1b[0m text")

print("This is \x1b[41m 41 \x1b[0m background")
print("This is \x1b[91m 91 \x1b[0m text")
print("This is \x1b[101m 101 \x1b[0m background")
print("This is \x1b[102m 102 \x1b[0m background")
print("This is \x1b[103m 103 \x1b[0m background")
print("This is \x1b[104m 104 \x1b[0m background")
print("This is \x1b[105m 105 \x1b[0m background")
print("This is \x1b[106m 106 \x1b[0m background")
print("This is \x1b[107m 107 \x1b[0m background")
print("This is \x1b[108m 108 \x1b[0m background")

print("This is \x1b[41m 41 \x1b[0m background") #green
print("This is \x1b[42m 42 \x1b[0m background") #green
print("This is \x1b[43m 43 \x1b[0m background") #yellow
print("This is \x1b[44m 44 \x1b[0m background") #blue
print("This is \x1b[45m 45 \x1b[0m background")  #purple
print("This is \x1b[46m 46 \x1b[0m background")  #lightgreen




