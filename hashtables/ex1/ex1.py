def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    """
    picked_weight & pairing_weight
    picked_weight = key
    pairing_weight = limit - picked_weight
    if picked_weight >, put in zero index.
    else put in first index.
    """
    pairing_weights = dict()

    for index in range(length):

        weight = weights[index]

        if weight in pairing_weights:

            previous_pairing_weight_index = pairing_weights[weight]

            return(index, previous_pairing_weight_index)

        pairing_weights[limit-weight] = index

    return None
