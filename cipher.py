#Given a string and a key, run that string through a cipher
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word= ''

#Prompt for a string or char
word = input("Enter a string:")

#Prompt for a number until we get one
while 1:
    try:
        key = int(input("Enter a key:"))
    except ValueError:
        print("Not a valid key")
    else:
        break

#Print out the new string after running through the cipher
for letter in word.lower():
    if letter.isalpha():
        try:
            print(alphabet[alphabet.index(letter)+key], end="")
        except:
            print(alphabet[alphabet.index(letter)+key-26], end="")
    else:
        print(' ', end="")
