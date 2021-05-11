str=input("enter the string:")
str=str[::-1]
print(str)
value=str
value_altered=''.join(chr(ord(letter)+1) for letter in value)
print(value_altered)
