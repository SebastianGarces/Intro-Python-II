# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def pick_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)

    def move(self, direction):
        new_room = self.current_room

        if direction == 'n':
            if self.current_room.n_to:
                new_room = self.current_room.n_to
        if direction == 's':
            if self.current_room.s_to:
                new_room = self.current_room.s_to
        if direction == 'e':
            if self.current_room.e_to:
                new_room = self.current_room.e_to
        if direction == 'w':
            if self.current_room.w_to:
                new_room = self.current_room.w_to

        if self.current_room.name != new_room.name:
            self.current_room = new_room
        else:
            print("\nWARNING: There is nothing in that direction! Try again.")
