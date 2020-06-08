from service import creator
from invoice import invoice

# items = ['ASC151 - Alpine Homes - Willow Glen – 115', 'Install 13 windows and 1 door', 'Willow Glen 1151892 E Janie CircleSaratoga Springs, Ut']


# find_items = items[1].split(" ")
# try:
#     win_index = find_items.index("window")
#     win_amt = find_items[(win_index - 1)]
# except:
#     win_index = find_items.index("windows")
#     win_amt = find_items[(win_index - 1)]
# try:
#     door_index = find_items.index("door")
#     door_amt = find_items[(door_index - 1)]
# except:
#     door_index = find_items.index("doors")
#     door_amt = find_items[(door_index - 1)]

# invoice(loc=items[0], window_amount=win_amt, amtofdoors=door_amt, desc_of_serv="test")
import os
for item in os.scandir("C:/Users/Ethon/Documents/Invoices"):
    print(item.name[23:-5])