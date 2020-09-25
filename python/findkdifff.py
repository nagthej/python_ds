


def find_k_diff(arr, k):
    #import pdb; pdb.set_trace()
    counter = 0


    dict = {}

    for num in arr:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1


    for k in dict.keys():
        if k+2 in dict:
            counter += 1


    if counter:
        print("{} distinct pairs exists".format(counter))
    else:
        print("no pairs")


#Driver code

arr = [3,1,4,1,5]
k = 2
find_k_diff(arr, k)

