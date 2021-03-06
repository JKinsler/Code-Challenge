def countElements(arr):
    """Given an integer array arr, count element x such that x + 1 is also in arr.
       If there're duplicates in arr, count them seperately.

       Example:
       >>> countElements([1,2,3])
       2
       >>> countElements([1,1,3,3,5,5,7,7])
       0
       >>> countElements([1,3,2,3,5,0])
       3
       >>> countElements([1,1,2,2])
       2
    """

    # start count at 0
    # check all the elements in the list
    # if the element of el+1 is also in the list
    # count add 1

    count = 0

    for el in arr:
        ele = el + 1

        if ele in arr:
            count += 1

    return count


#######################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")
