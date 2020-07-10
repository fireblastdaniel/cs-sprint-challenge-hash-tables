#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # pass through once to make a hashtable
    ticket_dict = {}
    for i in range(length):
        ticket_dict[tickets[i].source] = tickets[i].destination

    # make output array
    route = []
    current = ticket_dict["NONE"]
    while current != "NONE":
        route.append(current)
        current = ticket_dict[current]
    route.append(current)

    return route
