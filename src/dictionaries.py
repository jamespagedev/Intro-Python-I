"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with 
lists!). 

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
  - lat: a signed integer representing a latitude value
  - lon: a signed integer representing a longitude value
  - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
waypoints.append({"lat": 45, "lon": -124, "name": "new waypoint"})
print(waypoints)
print()

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# YOUR CODE HERE
for waypoint in waypoints:
    if (waypoint["name"] == "a place"):
        waypoint.update({"lon": -130, "name": "not a real place"})
        break
print(waypoints)
print()

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
# Student Question: What do you mean by all the field values??
#   All the values for the keys (e.g.: 41, -123, 'another place')
#   By field do you mean the keys (e.g.: 'lat', 'lon', 'name')
#   or by field do you mean only the 'lat' and 'lon' values (e.g.: 41, -123)
for waypoint in waypoints:
    print(list(waypoint))
    print(waypoint.keys())
    print(waypoint.values())
    print(waypoint.items())
    print([waypoint['lat'], waypoint['lon']])
    print()
