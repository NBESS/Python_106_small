### Small: Single hotel

# The goal of the small exercise is to get practice with the syntax for querying and manipulating the data in a single, nested dictionary.

# Write functions to:

# - is_vacant(which_hotel, '101')
#   - check if a room is occupied
# - check_in('101', guest_dictionary)
#   - assign a person to a room
# - check_out('101')
#   - returns the person dictionary in that room

# Please look back at any notes or slides for how to perform any of these actions. 

###

hotel = {
    '101': {},
    '102': {},
    '103': {},
    '104': {},
    '105': {},
}

# if hotel['101'] == {}:
#     print(f'Room 101 is vacant.')

# Create dictionary for each additional guest
# guest1 = {
#     'name': 'Tracy Ellis'
#     'phone': '3331234'
# }
hotel = {
     '101': {
        'guest': {
             'name': 'Peggy Sue',
             'phone': '3331234',
        }
     },
     '102': {},
     '103': {},
     '104': {},
     '105': {},
}

# if hotel['101'] == {}:
#     print(True)
# else:
#     print(False)


def is_vacant(hotel, room_number):
    if hotel[room_number] == {}:
        return f'Room {room_number} is vacant.' 

    else:
        return f'Room {room_number} is occupied'

print(is_vacant(hotel, '101'))
print(is_vacant(hotel, '102'))
print(is_vacant(hotel, '103'))