from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

items = {
    'pen': Item("Pen", "A pen is a common writing instrument used to apply ink to a surface, usually paper, for writing or drawing."),
    'sword': Item("Sword", "A small, slim, barbed blade made of folded steel is held by a grip wrapped in uncommon, maroon bear leather."),
    'book': Item('Book', 'The Bible, as we hold it today, is esteemed by many religious institutions and especially Conservative Christians to be the inspired, inerrant Word of God...'),
    'coin': Item("Coin", "A small, flat, round piece of metal or plastic used primarily as a medium of exchange or legal tender."),
    'torch': Item("Torch", "A burning stick of resinous wood or twist of tow used to give light and usually carried in the hand."),
    'bottle': Item("Bottle", "Container that is used to hold water, liquids or other beverages for consumption."),
    'thermometer': Item("Thermometer", "An instrument for measuring temperature, often a sealed glass tube that contains a column of liquid."),
    'pot': Item("Pot", "A container of earthenware, metal, etc., usually round and deep and having a handle or handles and often a lid, used for cooking, serving, and other purposes."),
    'mop': Item("Mop", "It is used to soak up liquid, for cleaning floors and other surfaces."),
    'watch': Item("Watch", "A watch is a portable timepiece intended to be carried or worn by a person."),
}

# Add items to rooms

room['outside'].add_item(items['pen'])
room['outside'].add_item(items['sword'])
room['foyer'].add_item(items['book'])
room['foyer'].add_item(items['coin'])
room['overlook'].add_item(items['torch'])
room['overlook'].add_item(items['bottle'])
room['narrow'].add_item(items['thermometer'])
room['narrow'].add_item(items['pot'])
room['treasure'].add_item(items['mop'])
room['treasure'].add_item(items['watch'])


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.


def get_user_choice():
    return input(choice_message)


def concat_items(items):
    result = ""
    for item in items:
        result += f"Name: {item.name}\nDescription: {item.description}\n\n"
    return result


def move_to(room, direction):
    new_room = room

    if direction == 'n':
        if room.n_to:
            new_room = room.n_to
    if direction == 's':
        if room.s_to:
            new_room = room.s_to
    if direction == 'e':
        if room.e_to:
            new_room = room.e_to
    if direction == 'w':
        if room.w_to:
            new_room = room.w_to

    return new_room


def get_user_name():
    username = input('\nEnter your username:\n')
    return Player(username, room['outside'])


playing = True
player = get_user_name()
choice_message = 'What would you like to do?\n[q] quit\n[drop {item_name}] drop an item\n[pick {item_name}] pick an item\n\nWhere would you like to go?\n[n] north\n[s] south\n[e] east\n[w] west\n\nYOUR CHOICE:  '
spacing = '\n-------------------------------------------------------\n'

while playing:
    items_list = f"{spacing}\nRoom items:\n\n{concat_items(player.current_room.items)}"
    player_inventory = f"Current inventory:\n\n{concat_items(player.inventory)}{spacing}"
    current_location = f"Location: {player.current_room.name}\nDescription: {player.current_room.description}"

    print(spacing)
    print(current_location)
    print(items_list)
    print(player_inventory)

    choice = get_user_choice().split(' ')

    if choice[0] == 'q':
        playing = False

    if playing:
        if choice[0] == 'n' or choice[0] == 's' or choice[0] == 'e' or choice[0] == 'w':
            player.move(choice[0])

        if len(choice) == 2 and choice[0] == 'drop':
            item = items[choice[1].lower()]
            player.drop_item(item)
            player.current_room.add_item(item)

        if len(choice) == 2 and choice[0] == 'pick':
            item = items[choice[1].lower()]
            player.pick_item(item)
            player.current_room.remove_item(item)


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
