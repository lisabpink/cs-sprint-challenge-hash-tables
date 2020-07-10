#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    Key: starting location
    Value: destination
    """
    # Your code here
    flight = dict()
    route = []

    for i in range(length):
        key = tickets[i].source
        value = tickets[i].destination

        flight[key] = value

    # If source = "NONE", is first ticket
    key = flight["NONE"]

    # If source is not first ticket
    while key != "NONE":
        route.append(key)

        key = flight[key]
    route.append(key)

    return route
