# You are given a list of string elements and asked to return a list which contains each element of the string in title case or in other words first character of the string would be in upper case and remaining all characters in lower case

# Sample Input:

# ['VARMA', 'raj', 'Gupta', 'SaNdeeP']



# Sample Output

# ['Varma', 'Raj', 'Gupta', 'Sandeep']


x=['VARMA', 'raj', 'Gupta', 'SaNdeeP']
y=str(x)
z=y.title()

for words in z:
    print(words,end="")


# for i in range(len(x)): # this line give as lenght of string like [0123]
#     y=x[i].title()
#     print(y)











