from bs4 import BeautifulSoup as bs
from service import creator
from invoice import invoice
import os

def scrape(html):
    items = []
    soup = bs(html, "html.parser")
    fonts = soup.find_all("font")
    for font in fonts:
        items.append(font.get_text())
    try:
        new_items = items[0].split("\xa0")
        clean_list = []
        for item in new_items:
            if item != "":
                clean_list.append(item)
        check_list = clean_list[0].split(" ")
        other_list = clean_list[1].split(" ")
        checker = True
        for item in os.scandir("C:/Users/Owner/Documents/Invoices"):
            if item.name[23:-5] == clean_list[0]:
                checker = False
        if checker:
            for check in check_list:
                if check == "Service":
                    
                    for item in other_list:
                        if item.lower() == "sash" or item.lower() == "sash.":
                            creator(loc=clean_list[0], trip_price=85, desc_of_serv=(clean_list[1] + " " + clean_list[2] + " " + clean_list[3]))
                        elif item.lower() == "adjust" or item.lower() == "replace":
                            creator(loc=clean_list[0], trip_price=85, desc_of_serv=(clean_list[1] + " " + clean_list[2] + " " + clean_list[3]))
                        elif item.lower() == "screen" or item.lower() == "screens" or item.lower() == "screens.":
                            creator(loc=clean_list[0], trip_price=95, desc_of_serv=(clean_list[1] + " " + clean_list[2] + " " + clean_list[3]))
                        elif item == "IG" or item == "IG.":
                            creator(loc=clean_list[0], trip_price=95, desc_of_serv=(clean_list[1] + " " + clean_list[2] + " " + clean_list[3]))
                            
                    
                    
                
                    

                    
                    return None
                else:
                    print(clean_list)
                    # invoice(loc=clean_list[0],desc_of_serv=(clean_list[1] + " " + clean_list[2] + " " + clean_list[3]))
                    return None
        else:
            print("already exists")
            
        # if service_item.lower() == "sash":
        #     
        # elif service_item.lower() == "screen":
        #     
        
    except:
        return None
        


