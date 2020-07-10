def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_by_index = {}

    for i in range(len(weights)):
        if limit - weights[i] in weight_by_index:
            return [i, weight_by_index[limit - weights[i]]]
        else: 
            weight_by_index[weights[i]] = i

    return None
