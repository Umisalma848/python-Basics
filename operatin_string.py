# operation in string and the string are immutable
a="salma"
b="SALMA"
c="!!!!!!!!!!!!!umi!!!  !!!!!!!!!!!!!!!! !!!!!!!!!!!!!!"
d="introduction to python"

print(a.upper())
print(b.lower())
print(c.rstrip("!"))          #rstrip      -remove special character of trailer 
print(c.replace("umi","me"))  #replace     -umi with me
print(c.split( " "))          #split       -work when the sentence having a gap it put , inbetweenand it treat like a one element
print(d.capitalize())         #capitalize  -making the first character in upper case
print(b.center(10))           #center      -it making the sentence in center align formate
print(c.count("umi"))         #count       -how many time the string will appear in a sentence 
print(c.endswith("!!!"))      #endswith    -it give an answer in true/false when the searching element in the last sentence exist or not
print(c.startswith("!!!"))    #startswith  -it give an answer in true/false when the searching element in the first sentence exist or not
print(d.find("to"))           #find        -it search the first element and give output as index if it is present , if not it return -1
print(d.index("duc"))         #index       -if it is in the string it give a index ottherwise -1
print(a.isalnum())            #isalnum     -if the string is made upof the element like A-Z, a-z,0-9 (alphanumeric)
print(a.isalpha())            #isalpha     -if the string is made upof the element like A-Z, a-z (alpha)
print(b.islower())            #islower     - the string are in lowercase or not
print(b.isupper())            #isupper     - the string are in uppercase or not
print(b.isprintable())        #isprintable -the string which do not have the /n,/t,// etc if have, the return is false
print(d.isspace())            #isspace     - if tthe string has white space it can be /t the return is true 
print(c.istitle())            #istitle     -title or not
print(d.title())              #title       - making all the first letter of word in the string in capital letter 
print(d.swapcase())           #swapcase    - convert upper case to lower case,and lower case to uppercase