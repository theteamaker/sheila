from search import provinces, cities, get_search_data
from titlecase import titlecase


def argument_constructor(argument):
    try:
        unformatted_split_argument = argument.split(" ")

        split_argument = []

        match_found = False
        for province in provinces.items():
            if unformatted_split_argument[0].lower() == province[1]["ID"].lower():
                split_argument.append(province[1]["ID"])

                match_found = (
                    True  # check for whether to continue on and parse the city or not
                )
                break

        if match_found is False:  # don't parse anything if something goes wrong
            return 404

        to_append = ""

        for index in range(len(unformatted_split_argument)):
            if index > 0:
                to_append += str(unformatted_split_argument[index])
                if (
                    index != len(unformatted_split_argument) - 1
                ):  # minor nuisance for providing whitespace appropriately
                    to_append += " "

        split_argument.append(to_append)

        provincial_ID = split_argument[0]
        city = split_argument[1]

        try:
            return [titlecase(city.lower()), cities[provincial_ID][city.lower()]]
        except:
            return 404
    except:
        return 404
