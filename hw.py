
def missing_elements(my_list: list) -> list:
    res = [ele for ele in range(max(my_list)+1) if ele not in my_list]
    return res[1:]

def count_occurrences(my_list: list) -> dict:
    freq = {}
    for item in my_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

def common_elements(list1: list, list2: list) -> list:
    freq = {}
    result_list = []
    for each in (list1 + list2):
        if each in freq:
            freq[each] += 1
        else:
            freq[each] = 1
    for item in freq:
        if freq[item] >= 2:
            result_list.append(item)
    return result_list


def char_frequency(my_string: str) -> dict:
    freq = {}
    for char in my_string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


def unique_words(my_string: str) -> int:
    words = my_string.split()  # Split the string into words
    unique_word_set = set(words)  # Create a set to store unique words
    return len(unique_word_set)  # Return the size of the set


def word_frequency(my_string: str) -> dict:
    my_string = my_string.strip()
    freq = {}
    if my_string == '':
        return freq
    for each in my_string.split(' '):
        if each in freq:
            freq[each]+= 1
        else:
            freq[each] = 1
    return freq


def count_in_range(my_list: list, start: int, end: int) -> int:
    unique_elements = set()
    for num in my_list:
        if start <= num <= end:
            unique_elements.add(num)
    return len(unique_elements)


def swap_dict(d: dict) -> dict:
    new_dict={}
    for key, value in d.items():
        new_dict[value] = key
    return new_dict


def is_subset(set1: set, set2: set) -> bool:
    return set2.issubset(set1)


def list_intersection(list1: list, list2: list) -> list:
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))


def list_union(list1: list, list2: list) -> list:
    return list(set(list1+list2))


def most_frequent(my_list: list) -> int:
    freq = {}
    for item in my_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    max_count = 0
    most_frequent_element = None
    for num, count in freq.items():
        if count > max_count:
            max_count = count
            most_frequent_element = num

    return most_frequent_element


def least_frequent(my_list: list) -> int:
    freq = {}
    for item in my_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    min_count = float('inf')
    least_frequent_element = None
    for num, count in freq.items():
        if count < min_count:
            min_count = count
            least_frequent_element = num

    return least_frequent_element

