def printMap():

    myList = [2, 12, 32, 42, 11, 1]
    ## Map to bool if number is greater than 10
    mapped_numbers = list(map(lambda x: x > 10, myList))
    ## filter numbers greater than 10
    filtered_numbers = list(filter(lambda x: x > 10, myList))
    ## reduce to greater number in list
    reduced_numbers = reduce(lambda x, y: x if x > y else y, myList)

    print (mapped_numbers)
    print (filtered_numbers)
    print (reduced_numbers)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    printMap()

