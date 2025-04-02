#This is only dummy data to test functions. The sqlite code will be present soon 

from hotel import Hotel
from hotel import Location
from user import User
from room import Room

rooms_tisia = [
    
    Room(1, 12000, True),
    Room(2, 13000, True),
    Room(3, 16000, True)
]

rooms_fonix = [ Room(1, 12000, True),
                Room(2, 13000, True),
                Room(3, 16000, True)]

rooms_veronica = [  Room(1, 17000, True),
                    Room(2, 13040, True),
                    Room(3, 16200, True)]

rooms_santiago = [Room(1, 12000, True),
                  Room(2, 132340, True),
                  Room(3, 16900, True)]


loc1 = Location("Hungary", "BAZ-megye", "Tiszaujvaros", "Tisza utca 12", 3580)
loc2 = Location("Hungary", "BAZ-megye", "Tiszaujvaros", "Debreceni út 2", 3580)
loc3 = Location("Hungary", "BAZ-megye", "Tiszaujvaros", "Kálmán tér 3", 3580)
loc4 = Location("United States", "Virginia", "New York", "Niggas street 32", 2333)

hotels = [
    
    Hotel(1,"Tisia",  loc1, 4, 20000, None, rooms_tisia),
    Hotel(2,"Főnix Hotel",  loc2, 2, 12000, None, rooms_fonix),
    Hotel(3,"Veronica Panzio",  loc3, 3, 14000, None, rooms_veronica),
    Hotel(4,"Santiago versacce",  loc4, 5, 91000, None, rooms_santiago)

]
users = [
    User("John Doe", 1, None, None),
    User("Jack Smith",2,None, None),
    User("Daniel Potter",3,None, None)
]

