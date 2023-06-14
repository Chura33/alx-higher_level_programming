#!/usr/bin/python3
def best_score(a_dictionary):
    array = list(a_dictionary.keys())
    largest = a_dictionary[array[0]]
    largest_key = array[0]
    for i in array:
        if a_dictionary[i] > largest:
            largest = a_dictionary[i]
            largest_key = i
    if largest_key:
        return largest_key
    return None

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

