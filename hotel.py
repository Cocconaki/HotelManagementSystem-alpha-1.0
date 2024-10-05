from user import User
from room import Room


class Location:
   def __init__(self, country, county, city, street_and_num, post_code ) -> None:
      self.country = country
      self.county = county
      self.city = city
      self.street_and_num = street_and_num
      self.post_code = post_code

   def __str__(self) -> str:
       return f"{self.country}, {self.county}, {self.city}, {self.street_and_num}, {self.post_code}"

class Hotel:

    def __init__(self, hotel_id, name:str, loc:Location, rate:int, price_per_room:int, residents=None, rooms_in_hotel=None) -> None:
        
        if residents is None:
           self.residents = []
        else:
           self.residents = residents
         
        if rooms_in_hotel is None:
           self.rooms_in_hotel = []
        else:
           self.rooms_in_hotel = rooms_in_hotel 

        self.hotel_id = hotel_id
        self.name = name
        self.loc = loc
        self.rate = rate
        self.price_per_room = price_per_room

    def show_data(self):
        
      print(f"Name: {self.name}\n"
            f"rooms available: {len(self.rooms_in_hotel)}\n"
            f"Location: {self.loc}\n"
            f"RATING: {self.rate}\n"
            f"Price of rooms: {self.price_per_room}\n")
    
    def show_by_rating(self, rate_inp):
       if self.rate >= rate_inp:
          self.show_data()

    def show_by_loc(self, loc_inp):
       if self.loc.city == loc_inp:
          self.show_data()
    
    def show_rooms(self):
       print(f"Number of rooms available: [{len(self.rooms_in_hotel)}] --- @{self.name}") 