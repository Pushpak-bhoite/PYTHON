st  = " MAHARANA "

for ch in st :
    print(ch)
    
print("Rest of the code ")

# ****For loop with Range****   range is only accepts integers

st = range(5)
for ch in st :
    print(ch)
print("Reast of the code")

# ****For with String*****

str = "Mahabharat"
n = len(str)
for i in range(n) :    #range(n) = 10(i.e length of string )
    print(i," : ",str)
    print(i," : ",str[i])

# break : break statement breaks code permanantly since use the break
# continue : Is only use for skip specific statement