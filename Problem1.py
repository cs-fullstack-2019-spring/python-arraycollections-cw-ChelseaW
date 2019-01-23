def main():
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    problem5()
#     Create a function with the variable below. After you create the variable do the instructions below that.
#
# arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
# a) Print the 3rd element of the numberList.
#
#     b) Print the size of the array
#
# c) Delete the second element.
#
#     d) Print the 3rd element.

# Function is printing size and removing element from the array

# def problem1():
#
#     arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
#     print(arrayForProblem2[3])
#     print(len(arrayForProblem2))
#     arrayForProblem2.remove(2)
#     print(arrayForProblem2[3])



    # Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
# def problem2():
#     creator = ""
#     while creator != 'q':
#       creator = input("Something weird")
#       print(creator)




# Create a function that contains a collection of information for the following. After you create the collection do the instructions below that.
#
# Jonathan/John
# Michael/Mike
# William/Bill
# Robert/Rob
# a) Print the collection
#
# b) Print William's nickname

# def problem3():
#
#     theCrew = {
#         "Jonathan": " John",
#         "Michael":" Mike",
#         "William":"Bill",
#         "Robert":"Rob"
#     }
#     print(theCrew)
#     print(theCrew["William"])




# Create an array of 5 numbers. Using a loop, print the elements in the array reverse order. Do not use a function
# def problem4():
#
#
#     digits = [20,12,19,69,88]
#     for eachElement in range(len(digits)-1,-1,-1):
#         print(digits[eachElement])

    # for eachEl in range(0, len(digits)-1, 1)

    # range(0,5) = [0,1,2,3,4]


    # for eachEl in range():
    #         print(digits[eachEl])

    # for digits in range(-88,11):
    # reversed(digits)
        # digits -+1
        #     print(digits)


# Create a function that will have a hard coded array then ask the user for a number.
# Use the userInput to state how many numbers in an array are higher, lower, or equal to it.

def problem5():

   listOfDigits = [1,2,3,4,5]:
   listOfDigits = input("Give a number")
   # print(listOfDigits(1))
   # print(listOfDigits(4))
   # print(listOfDigits(5))

   higher = 0
   lower= 0
   equal = 0



   for eachElement in listOfDigits():
    if(listOfDigits== eachElement):
         +=1
        print("Lower")
    if(listOfDigits== eachElement):
        fourCount +=1
        print("Equal")
    if(listOfDigits== eachElement):
        fiveCount +=1
        print("Higher")







if __name__ == '__main__':
    main()