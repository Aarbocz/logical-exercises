# Label apartments based on floor number and apartment per floor

# Get number of floors and apartment per floor
floors = int(input("Number of floors: "))
apartments = int(input("Number of apartments per floor: "))

# Stores floors and apartments numbers
building = {}

# Get multiplier dependin on number of apartments
apt = apartments
multiplier = 1
while(apt>0):
    multiplier = multiplier * 10
    apt = apt // 10

# Populate building dict
for floor in range(floors):
    building[floor + 1] = []
    for apartment in range(apartments):
        building[floor + 1].append((floor + 1) * multiplier + apartment + 1)

# Print results
for key, value in building.items():
    print()
    print(f"Floor: {key}: {value}")