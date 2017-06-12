def index_list(index, length_cipher):

    index_list = []
    #loop through a range as big as the cipher list
    for i in range(length_cipher):
        #create a new list with the index word
        index_list += (index[i % (len(index))])
        #convert the letters into ordinal numbers
        index_list[i] = ord(index_list[i])
        #account for capitals
        cap = 97 if index_list[i] > 96 else 65
        index_list[i] = index_list[i] - cap

    return index_list


def add_lists(cipher_list, list_index):
    summed_list = []
    for i in range(len(cipher_list)):
        summed_list = summed_list + [((cipher_list[i]+list_index[i])%26)]

    return summed_list
