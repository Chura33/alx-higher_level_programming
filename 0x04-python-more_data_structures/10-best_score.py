#!/usr/bin/python3
def best_score(a_dictionary):
    array = a_dictionary.keys()
    largest = a_dictionary[array[0]]
    largest_key = array[0]
    for i in array:
        if a_dictionary[i] > largest:
            largest = a_dictionary[i]
	    largest_key = i
    if (largest and largest_key):
        return (largest_key)
    return (None)

