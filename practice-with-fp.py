'''
Problem 1: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

>>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
{'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
'''


def flatten_dict(dictionary):
    flattened = {}
    for key in dictionary.keys():
        if isinstance(dictionary[key], dict):
            for inner_key, inner_value in dictionary[key].items():
                flattened.update({key + "." + inner_key: inner_value})
        else:
            flattened.update({key: dictionary[key]})
    return flattened


print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}}))


'''
Problem 2: Write a function unflatten_dict to do reverse of flatten_dict.

>>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
{'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
'''


def unflatten_dict(d):
    """Unflattens a nested dictionary. (reverses flatten_dict)
    keys must be strings in all dictionaries for this to work.
      """
    result = dict()
    for i in d.keys():
        if "." in i:
            # this should become nested
            new_key, sep, inner_key = i.partition(".")
            # create dictionary if not yet created
            if new_key not in result.keys():
                result[new_key] = dict()
            # add elements to inner dictionary
            result[new_key][inner_key] = d[i]
        else:
            # add the k:v pair to result dictionary
            result[i] = d[i]
    return result


print(unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}))


'''
Problem 3: Write a function treemap to map a function over nested list.

>>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
[1, 4, [9, 16, [25]]]
'''


def treemap(func, lst):
    for i in range(len(lst)):
        if type(lst[i]) == list:
            lst[i] = treemap(func, lst[i])
        else:
            lst[i] = func(lst[i])

    return lst


print(treemap(lambda i: i*i, [1, 2, [3, 4, [5]]]))
