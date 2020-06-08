from service import creator

def checker(l):
    clean_list = l
    variables = clean_list[1].split(" ")
    for item in variables:
        if str(item).lower() == "sash":
            creator(loc=clean_list[0], trip_price=85, desc_of_serv=(clean_list[1] + " " + clean_list[2] + " " + clean_list[3]))
        elif str(item).lower() == "screens" or "screen":
            creator(loc=clean_list[0], trip_price=95, desc_of_serv=(clean_list[1] + " " + clean_list[2] + " " + clean_list[3]))
        else:
            print("what?")