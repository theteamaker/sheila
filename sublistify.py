
def sublistify(unsplit_list, amount):
    average_amount = len(unsplit_list) // amount #defines the average amount each list should have

    sub_lists = []
    to_add = []

    for iteration in range(amount):
        if iteration + 1 != amount:
            while len(to_add) < average_amount:
                to_add.append(unsplit_list[0])
                unsplit_list.remove(unsplit_list[0])
            if len(to_add) == average_amount:
                sub_lists.append(to_add.copy())
                to_add.clear()
                continue
        else:
            while len(unsplit_list) != 0:
                to_add.append(unsplit_list[0])
                unsplit_list.remove(unsplit_list[0])
            if len(unsplit_list) == 0:
                sub_lists.append(to_add.copy())
                to_add.clear()

    return sub_lists