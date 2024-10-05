from dataclasses import dataclass, field


@dataclass
class Room:

   room_number:int
   price_per_night:int
   is_available:bool = field(default=True)