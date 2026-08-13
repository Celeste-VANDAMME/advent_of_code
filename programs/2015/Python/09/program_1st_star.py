# [>] LIBRARIES
# ---------------------
from pathlib import Path



# [>] GLOBAL VARIABLES
# ---------------------
input_path = Path("programs/2015/Python/09/sample.txt")


# [>] FUNCTIONS
# ---------------------
def file_reading() -> list[str]:

    data = input_path.read_text(encoding="utf-8").splitlines()
    return data


def r_path_calculator(
        current_city:str, 
        not_visited_city:list[str], 
        city_global_info:dict[str, dict[str, int]] 
        ) -> float:

    if( len(not_visited_city) == 0):
        print(f"   [EoT] Reached the end on {current_city}!")
        return 0

    # OTHERWISE: We have more cities to explore!
    smaller_distance:float = float("inf")


    for next_city, distance in city_global_info[current_city].items():
        print(f"\t[>>> l2] Check: {next_city} ({distance})")

        if next_city in not_visited_city:
            
            remaining_city_not_visited = not_visited_city.copy()
            remaining_city_not_visited.remove(next_city)

            print(f"\t   [!]MATCH: GOING INTO {next_city} exploration! (remaining city: {remaining_city_not_visited})")
            distance_calculation_try = distance + r_path_calculator(next_city, remaining_city_not_visited, city_global_info)

            smaller_distance = min(smaller_distance, distance_calculation_try)



    return smaller_distance

    
    


def shortest_path(city_global_info:dict[str, dict[str, int]]) -> float:

    # Let's set a list of all the city we need to go through
    # Using this list, we can go through each city one by one (by removing a city upon
    # visiting it).
    city_listing = list(city_global_info.keys())


    # Display
    '''
    for city_info in city_global_info:
        print (city_info, city_global_info[city_info])
    
    # print( "LIST OF UNIQUE CITIES TO GO THROUGH:", city_listing )
    '''

    # 1. We cycle through all cities available in the whole file.
    # >> This has flaws, because we're going to check the same path twice.
    # Example: A>B>C>D once, then D>C>B>A another loop. But it's okay for now.

    # 2. Starting from this city, we will cycle through ALL other cities linked to it.
    # Example:  A > B > C > ...
    #               B > E > ...
    #
    #           A > C > B > ...
    #             > C > D > ...
    #
    # 3. Then, we will keep going through the same process with the cities found.
    # However, because we can only go ONCE in each city, we won't take into account the 
    # cities we've already been through (like A in our example).
    # This is done by having the complete city list at the begining, then removing a city upon visited.

    
    # path_global_trajectory: list[tuple[list[str], int]] = []
    # [ (["A", "B", "C", ...], 45), (.......) ]
    #    -------------------------  ---------
    #             list[0]            list[1]

    smallest_distance:float = float("inf")

    
    for starting_city in city_global_info:

        city_to_check = city_listing.copy()
        city_to_check.remove(starting_city)

        print(f"\n[>> LOOP 1] CITY START: {starting_city}")

        # Recursive Function?
        branch_distance = r_path_calculator(starting_city, city_to_check, city_global_info )

        smallest_distance = min(smallest_distance, branch_distance)

        print(f" [*] Smallest distance so far? {smallest_distance}")
        


    return smallest_distance


# [>] main()
# ---------------------
def main() -> int:

    # Reading data
    data = file_reading()


    # [>>] Creating a database dict for all the cities and their connections
    # ---------------------
    city_global_info: dict[str, dict[str, int]] = {}


    for line in data:

        line_details = line.split()

        city_origin = line_details[0]
        city_destination = line_details[2]
        city_distance = int(line_details[4])

        # The origin city to have: {Origin : [Destination > Distance] }
        if city_origin in city_global_info:
            city_global_info[city_origin][city_destination] = city_distance


        else:
            city_global_info[city_origin] = {
                city_destination: city_distance
            }

        # The other city (destination) to reference everything:
        # The destination city to have: {Destination: [Origin > Distance] }
        if city_destination in city_global_info:
                city_global_info[city_destination][city_origin] = city_distance

        else:
            city_global_info[city_destination] = {
                city_origin: city_distance
            }


    # I went blind here, haven't checked any known algorithm for tree exploration.
    # I want to see where I land by myself, so brace incredibly not optimized code.

    # I'll go through each city in my list, and explore EACH possibilities

    print(f"[> GLOBAL] ALL PATHS AVAILABLES:\n{city_global_info}\n")

    shortest_path_distance = shortest_path(city_global_info)

    print( f"[>>>] Shortest distance: {shortest_path_distance}km!" )



    # [>] End of main()
    # ---------------------
    return 0



# [>] main() launcher
# ---------------------
if __name__ == "__main__":
    main()
    









