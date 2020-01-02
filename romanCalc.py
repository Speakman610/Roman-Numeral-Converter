i = 1
I = 1
v = 5
V = 5
x = 10
X = 10
l = 50
L = 50
c = 100
C = 100
d = 500
D = 500
m = 1000
M = 1000

romanNumeral = input ("Enter roman numeral for conversion here: ")
finalNumeral = 0
n2 = 0

for character in romanNumeral [ : :-1]:
    n1 = eval(character)
    if n2 <= n1:
        finalNumeral = n1 + finalNumeral
        n2 = n1
    if n2 > n1:
        finalNumeral = finalNumeral - n1

print (romanNumeral, " = ", finalNumeral)
