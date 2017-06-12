from helpers import index_list, add_lists

def encrypt(string, index):

    #if nothing is entered for index, restart function and ask for input of keyword
    if index == "":
        print( "Index must have value" )
        return vig(string, (input("Type in your keyword: ")))


    new_string = ""
    orig_cipher_list = []
    cipher_list = []
    count = 0

    #iterate through the string, letter by letter
    for letter in string:
        #check if letter is a character
        if not letter.isalpha():
            #if not, add that thing to the new list
            new_string += letter
        #otherwise, ceasar cipher!
        else:
            #conver letter to ord number
            letter = ord(letter)
            orig_cipher_list += [letter]
            #Account for Capitals vs Lowercase
            cap = 97 if letter > 96 else 65
            #subtract the cap to make the range easy
            letter -= cap
            #populate the string list to be compared to
            cipher_list += [letter]

            length_cipher = len(cipher_list)
            #create a list from the index word, as long as the cipher list

            #funtion to get a list of the index, the same as the cipher list
            list_index = index_list(index, length_cipher)
            #function to add the cipher list to the index list
            final = add_lists(cipher_list, list_index)
            #iterate through the added list, accounting for CAPS and chage back to a letter
            for number in range(len(final)):
                if orig_cipher_list[number] <= 84:
                    final[number] += 65
                else:
                    final[number] += 97
                final[number] = chr(final[number])
            new_string += final[count]
            count += 1
    return new_string

def main():
    '''This is the main function '''
    result = encrypt("BaRFoo", "BaZ")
    result2 = encrypt("The crow flies!", "Boom")
    #result = encrypt((input("Type a message: ")), (input("Type in your keyword: ")))
    print(result)
    print(result2)

if __name__ == '__main__':
    main()
