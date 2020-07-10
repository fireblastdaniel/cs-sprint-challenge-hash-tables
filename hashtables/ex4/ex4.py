def has_negatives(a):
    """
    YOUR CODE HERE
    """
    my_dict = {}
    result = []
    for item in a:
        if item in my_dict:
            result.append(abs(item))
        else:
            my_dict[item * -1] = item

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
