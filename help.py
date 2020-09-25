
import pdb

def ifStrUnique(str):
    #pdb.set_trace()

    if len(str) == 1:
        print("{} has unique chars".format(str))
        return

    if len(str) > 128:
        print("{} does not have unique chars".format(str))
        return


    ascii_std_list = []

    for i in range(128):
        ascii_std_list.append(False)

    for char in range(len(str)):
        ch_in_int = ord(str[char])
        if ascii_std_list[ch_in_int] == True:
            print("{} does not have unique chars".format(str))
            return
        else:
            ascii_std_list[ch_in_int] = True

    print("{} has unique chars".format(str))


#driver code

ifStrUnique("abclkj")