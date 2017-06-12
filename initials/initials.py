def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here

    name_list = fullname.split(" ")
    initial_name = ""
    for i in name_list:
        initial_name = initial_name + i[:1]
    return initial_name.upper()


def main():
    full_name = input("what is your full name?")

    result = get_initials(full_name)
    print(result)    

if __name__ == '__main__':
    main()

