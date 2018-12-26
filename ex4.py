spaceships = 200
cargo_space_in_a_spaceship = 50.0
space_captains = 60
passengers = 180
spaceships_not_driven = spaceships - space_captains
spaceships_driven  = space_captains
spaceship_capacity = spaceships_driven * cargo_space_in_a_spaceship
average_passengers_per_spaceship = passengers / spaceships_driven

print("There are ", spaceships, " spaceships available")
print("There are only ", space_captains, " space captains left")
print("There will be", spaceships_not_driven, "spaceships available for the future")
print("we can save only", spaceship_capacity, "beings today")
print("We have", passengers, "to save today")
print("We need  to transport about", average_passengers_per_spaceship, "to each ship in orbit")

