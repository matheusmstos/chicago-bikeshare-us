
# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")

for row in range(0, 21, 1):
    print(data_list[row])

# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("Press Enter to continue...")
# TASK 2
# TODO: Print the `gender` of the first 20 rows
print("\nTASK 2: Printing the genders of the first 20 samples")

gender_index = -2
for row in range(21):
    print(data_list[row][gender_index])

# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order


def column_to_list(data, index):
    """
    This function takes a column(feature) of a list and turns it to a line.
    Args:
      data: Receives a list.
      index: The position of the desired column.
    Returns:
      A list of a single feature.
    """
    column_list = []
    # Tip: You can use a for to iterate over the samples,
    # get the feature by index and append into a list
    for row in range(0, len(data), 1):
        column_list.append(data[row][index])
    return column_list

# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0

for row, item in enumerate(data_list):
    if data_list[row][-2] == "Male":
        male += 1
    elif data_list[row][-2] == "Female":
        female += 1


# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)


def count_gender(data_list):
    """
    This function counts the amount of "Gender" of a list.
    In our case, we have "Female" and "Male" as genders.
    Args:
      data_list: Receives a list containing strs "Female" and "Male".
    Returns:
      A list containing the amount of each gender.
    """

    male = 0
    female = 0

    for row, item in enumerate(data_list):
        if data_list[row][-2] == "Male":
            male += 1
        elif data_list[row][-2] == "Female":
            female += 1
    return [male, female]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.


def most_popular_gender(data_list):
    """
    This function counts the amount of "Gender" of a list.
    In our case, we have "Female" and "Male" as genders.
    Args:
      data_list: Receives a list containing strs "Female" and "Male".
    Returns:
      A str containing the gender with highest number.
    """

    answer = ""
    gender_list = count_gender(data_list)

    if gender_list[0] > gender_list[1]:
        answer = "Male"
    elif gender_list[0] < gender_list[1]:
        answer = "Female"
    else:
        answer = "Equal"
    return answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
user_type_list = column_to_list(data_list, -3)



def count_user_type(data_list):
    """
    This function counts the amount of "User Type" of a list.
    In our case, we have "Customer" and "Subscriber" as user types.
    Args:
      data_list: Receives a list containing strs "Customer" and "Subscriber".
    Returns:
      A list with the amount of "Customer" and "Subscriber".
    """

    customer = 0
    subscriber = 0

    for row, item in enumerate(data_list):
        if data_list[row][-3] == "Customer":
            customer += 1
        elif data_list[row][-3] == "Subscriber":
            subscriber += 1
    return [customer, subscriber]

print("\nTASK 7: Check the chart!")
print("Result of count_user_type:\n{}".format(count_user_type(data_list)))

types = ["Customer", "Subscriber"]
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('User Type')
plt.xticks(y_pos, types)
plt.title('Quantity by User Type')
plt.show(block=True)


input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
print("Male + Female = {} and len(data_list) = {}".format((male+female), len(data_list)))
answer = "Not all genders are filled."
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
trip_duration_list = column_to_list(data_list, 2)
int_trip_duration_list = [int(duration_str) for duration_str in trip_duration_list]

min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

def min_list(data_list):
    """
    This function calculates the minimum value of a list.
    Args:
      data_list: Receives any list.
    Returns:
      Min value of the list.
    """

    min_value = 0
    for list_num in data_list:
        if min_value == 0:
            min_value = list_num
        elif list_num < min_value:
            min_value = list_num
    return min_value

def max_list(data_list):
    """
    This function calculates the maximum value of a list.
    Args:
      data_list: Receives any list.
    Returns:
      Max value of the list.
    """

    max_value = 0
    for list_num in data_list:
        if list_num > max_value:
            max_value = list_num
    return max_value


def mean_list(data_list):
    """
    This function calculates the mean value of a list.
    Args:
      data_list: Receives any list.
    Returns:
      Mean value of the list.
    """

    sum_list = 0
    for num in data_list:
        sum_list += num
    mean_value = round(sum_list/len(data_list))
    return mean_value


def median_list(data_list):
    """
    This function calculates the median value of a list.
    Remembering that the list needs to be sorted and of integers.
    Args:
      data_list: Receives any list.
    Returns:
      Median value of the list.
    """

    n = len(data_list)
    if n%2 == 1: #odd size = even positions, len(n) = 5 -> [0..4]
        median_value = sorted(data_list)[n//2]
        #print("Length of the list: {} Median's position: {}".format(n, n//2))
    else:
        median_value = (sorted(trip_duration_list)[n//2 -1] +
                        sorted(trip_duration_list)[n//2])/2.0
        #print("Length of the list = {} Median's position = {} & {}".format(n, n//2 -1,n//2))
    return median_value

min_trip = min_list(int_trip_duration_list)
max_trip = max_list(int_trip_duration_list)
mean_trip = mean_list(int_trip_duration_list)
median_trip = median_list(int_trip_duration_list)

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about
#start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
#Remember: sets has no duplicates and it's unordered, wich means that there's no position[n]
user_types = set(column_to_list(data_list, 3))

# for row in enumerate(data_list):
#     user_types.add(data_list[row][3])

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output
 #and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
"""
Example function with annotations.
Args:
  param1: The first parameter.
  param2: The second parameter.
Returns:
  List of X values

"""

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "yes"


def count_items(column_list):
    """
    Function that counts user types without hardcoding the types.
    Args:
      colomn_list: A list of features.
    Returns:
      List of the types encoutered in the list and another list
      with how many are them.
    """

    item_types = []
    count_items = []
    for item in column_list:
        if item not in item_types:
            item_types.append(item)
            count_items.append(1) #count for the first time
        else:
            count_items[item_types.index(item)] += 1
    return item_types, count_items


if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------
