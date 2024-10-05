import os
import time
import logging
from data import *
from room import Room



class User:
    usr_id = set()
    def __init__(self,name:str, user_id:int, booked_room=None, book_cost=None) -> None:
            
            if user_id in User.usr_id:
                 raise ValueError(f"{user_id} is already taken.")
            User.usr_id.add(user_id)
            self.name = name
            self.user_id = user_id
            if book_cost is None:
                  self.book_cost = 0
            else:
                  self.book_cost = book_cost
            if booked_room is None:
                 self.booked_room = []
            else:
                 self.booked_room = booked_room
    
    def show_data(self):
         print(f"Name:{self.name}\n"
               f"ID:{self.user_id}\n"
               f"Costs:{self.book_cost}\n"
               f"Rooms:{self.booked_room}")
    
   
    
class ManageUsers:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def create_user():
      while True:
        try:
            name = str(input("Enter name: "))
            usr_id = int(input("Enter ID: "))
            return User(name, usr_id, None)
        
        except ValueError as e:
             print(e)
    
    @staticmethod 
    def delete_user():
        usr_to_delete = int(input("Enter user's ID: "))
        
        return usr_to_delete
        
    @staticmethod
    def show_usr_info():
         pass
    
    @staticmethod
    def add_room_to_user(hotel_rooms, costumer, hotel_is):
        
        valid_ID = [room.room_number for room in hotel_rooms]

        room_ID = int(input("Enter room ID to add: "))
        if room_ID not in valid_ID:
             print("Invalid number")
             return
        
        for_nights = int(input("Enter number of nights the costumer will stay: "))
        
        
        for room_item in hotel_rooms:
             if room_ID == room_item.room_number and room_item.is_available:
                  if costumer.booked_room is None:
                       setattr(costumer, "booked_room", [])
                       costumer.booked_room.append(room_item)
                       room_item.is_available = False
                  
                  elif costumer.booked_room is not None:
                       costumer.booked_room.append(room_item)
                       room_item.is_available = False


             elif not room_item.is_available:
                  print("Room is already taken")
                  return
        
        costumer.book_cost += room_item.price_per_night * for_nights
        costs_for_room = room_item.price_per_night * for_nights
        print(f"Room number {room_ID} was succesfully booked for costumer {costumer.user_id} at {hotel_is.name}")
        print(f"Costs of booking:{costs_for_room}")
        print(costumer.booked_room)
        input("press ENTER: ")
                  

    
