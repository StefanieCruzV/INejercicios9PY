# print all integers from 1 to 255
for i in range(1, 256):
    print(i)
print("---------------------------------")
# Print integers from 0 to 255, and with each integer print the sum so far.
# num: 0, sum:0
# num: 1, sum:1
# num: 2, sum:3
# num: 3, sum:6
sum = 0
for i in range(0, 256):
    # sum = sum + i
    sum += i
    print(f"num: {i}, sum:{sum}")

print("---------------------------------")

# Given an array, find and print its largest element.


def largestElement(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    print(max)


myList = [4, 9, -1, 0, 0, 14, 9, 8, 19, 100, -43, 98]
largestElement(myList)
myList2 = [4, 9, -1, 0, 0, 14, 945, 8, 19, 100, -43, 98]
largestElement(myList2)
myList3 = [-4, -9, -1, -3]
largestElement(myList3)
print("---------------------------------")

# Create an array with all the odd integers between 1 and 255 (inclusive).
odds = []
for i in range(1, 256):
    if i % 2 == 1:
        odds.append(i)
print(odds)
print("---------------------------------")

# Given an array and a value Y, count and print the number of array values greater than Y.


def greaterCount(list, y):
    count = 0
    for val in list:
        if val > y:
            print(val)
            count += 1
    print(count)


list4 = [4, 9, -1, 0, 0, 14, 9, 8, 19, 100, -43, 98]
greaterCount(list4, 10)
print("---------------------------------")

# Given an array, print the max, min and average values for that array.


def max_min_average(list):
    max = list[0]
    min = list[0]
    sum = 0
    avg = 0
    for i in list:
        sum += i
        if i < min:
            min = i
        if i > max:
            max = i
    avg = sum/len(list)
    print(f"max: {max}, min {min} , ave {avg}")


myList4 = [4, 9, -1, 0, 0, 14, 9, 8, 19, 100, -43, 98]
max_min_average(myList4)
myList5 = [4, 9, -1, 0, 0, 14, 945, 8, 19, 100, -43, 98]
max_min_average(myList5)
myList6 = [-0, 10, 5, 10, 5, 0]
max_min_average(myList6)
print("---------------------------------")

countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]

# Challenge 1: Fix the range!
for integer in range(0, len(countries)):
    print(f"Index: {integer}")
    # Challenge 2: print the index here
    print(f"Country: {countries[integer]}")
    # Challenge 3: print the country here

# Looping over values only...
for country in countries:
    print(f"Country:{country} ")
    # Challenge 4: print the country here

print("---------------------------------")

def multiply(num_list,num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# >>>[10,20,50,80]

