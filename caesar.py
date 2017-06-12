def rotate_character(letter, rot):
    #convert the letter to it's ordinal number
    letter = ord(letter)
    #Account for Capitals vs Lowercase in the ordinal range
    cap = 97 if letter > 96 else 65
    #subtract the cap to make the range easy (0-25).
    #Add the rotation, modulo 26 to keep in range
    number = ((letter - cap) + rot) % 26
    #add the cap back to the number, convert back to a letter, add into the new string.
    number = chr(number+cap)
    return number


def encrypt(string, rot):
    new_string = ""
    for letter in string:
    #check to see if what's passed in is actually a letter
        if not letter.isalpha():
            #if not, just add it into the string
            new_string += letter
        else:
            #convert letter to ord number
            new_string = new_string + rotate_character(letter, rot)
    #return the new mixed string
    return new_string


def main():
    result = encrypt(input("Type a message:"), int(input("Rotate by:")))
    print(result)

if __name__ == '__main__':
    main()
