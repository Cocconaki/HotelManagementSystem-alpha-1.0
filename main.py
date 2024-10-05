import os
import time

from data import *
from hotel import Hotel
from user import ManageUsers

while True:
    os.system("clear")
    print("List all hotels: (1) \n"
          "List hotels by rating: (2) \n"
          "Sort hotels by ratings: (3) \n"
          "Sort hotels by location: (4)\n"
          "Search for hotel by name: (5)\n"
          "Go to user management menu: (0)\n"
          "Exit (6)"                               )
          

    try:
        usr_input =int(input("Enter: "))
        match usr_input:
            case 1:
                os.system("clear")
                for hotel_item in hotels:
                    hotel_item.show_data()
                input("press ENTER: ")
            case 2:
                os.system("clear")
                rates = {hotel_item.name:hotel_item.rate for hotel_item in hotels}
                sorted_rates = dict(sorted(rates.items(), key=lambda item: item[1]))
                print("SORTED BY RATINGS:")
                for key, value in sorted_rates.items():
                    print(f"{key}: RATING[{value}]STAR")
                input("press ENTER: ")

            case 3:
                os.system("clear")
                rate_in = int(input("Enter rating: "))
                for hotel_item in hotels:
                    if hotel_item.rate == rate_in:
                        print(f"{hotel_item.name}:{hotel_item.rate}")
                        input("Press ENTER: ")
                    else:
                        print(f"No {rate_in} rated hotel was found...")
                        print("Directing back to menu...")
                        time.sleep(3)
                        break
                
            case 4:
                os.system("clear")
                location_search = str(input("Enter location to search for: "))
                for hotel_item in hotels:
                    if hotel_item.loc.city == location_search:
                        hotel_item.show_data()
                        input("press ENTER: ")
                    else:
                        print(f"No hotel was found at {location_search}")
                        print("Directing back to main menu...")
                        time.sleep(3)
                        break
            
            case 5:
                name_search = str(input("Search for hotel: "))
                os.system("clear")
                for hotel_item in hotels:
                    if hotel_item.name == name_search:
                        hotel_item.show_data()
                        input("Press ENTER: ")
                        break
                        
                    else:
                        print(f"No hotel named {name_search} was found")
                        print("Directing back to menu...")
                        time.sleep(3)
                        break
            case 6:
                break
                #----USER MANAGEMENT MENU-----
            case 0:
                
                while True:
                    os.system("clear")
                    print("Show users: (1)\n"
                      "Create user: (2)\n"
                      "Delete user: (3)\n"
                      "Back to main menu: (4)\n"
                      #####-new functionalities to implement-#####
                      "Book room for user: (5)\n" #DONE
                      "Delete room for user: (6)\n" #NOT DONE
                      "Pay for room with user: (7)\n") #NOT DONE
                    
                    usr_input = int(input("ENTER: "))
                    
                    match usr_input:
                        case 1:
                            os.system("clear")
                            for usr in users:
                                usr.show_data()
                            input("press ENTER: ")
                        case 2:
                            x = ManageUsers.create_user()
                            users.append(x)
                        case 3:
                             x = ManageUsers.delete_user()
                             for user_item in users:
                                 if user_item.user_id == x:
                                     users.remove(user_item)
                        case 4:
                            break
                        case 5:
                            while True:
                                os.system("clear")
                                #checks for valid hotel realted inputs
                                chose_hotel = input("Enter which hotel you'd like to choose from: ")
                                valid_names = [hotel.name for hotel in hotels]
                                
                                if chose_hotel not in valid_names:
                                    print(f"No hotel named {chose_hotel} was found")
                                    break
                                
                                hotel_chosen = None
                                for hotel_item in hotels:
                                    if hotel_item.name == chose_hotel:
                                        hotel_rooms = hotel_item.rooms_in_hotel
                                        hotel_chosen = hotel_item
                                
                                #check for valid user related inputs
                                valid_ID = [user.user_id for user in users]

                                chose_user = int(input("Enter users ID: "))
                                user_chosen = None
                                
                                if chose_user not in valid_ID:
                                    print("User does not exist")
                                    break

                                for user_item in users:
                                    if user_item.user_id == chose_user:
                                        user_chosen = user_item
                                
                                ManageUsers.add_room_to_user(hotel_rooms, user_chosen, hotel_chosen)

                            
                            
                        case 6:
                            pass
                        case 7:
                            pass
        
    
    except ValueError:
        print("Invalid value")
