# Python Dictionaries
# Used to store data in Key/Value pairs
# Looks similar to JSON Object

band = {
    "vocals": "Percy",
    "guitar": "Miggy",
}

band2 = dict(vocals="Percy", guitar="Miggy")

print(band)
print(band2)

# Access items
print(band['vocals'])
print(band.get('guitar'))

# List all Keys
print(band.keys())

# List all Values
print(band.values())

# List of pairs as tuples
print(band.items())

# Verify Key exists
print("guitar" in band)
print("drums" in band)

# Change values
band['vocals'] = "Cody"
print(band)
band.update({"drums": "Percy"})
print(band)

# Remove Items
print(band.pop('drums')) # Returns Value for specified Key, removes
print(band)

band['drums'] = "Percy"
print(band)

print(band.popitem()) # Last item returned as tuple, removed
print(band)

# Delete and clear
band["drums"] = "Percy"
del band["drums"] # Delete specified pair
print(band)

band2.clear()
print(band2)
del band2 # Delete entire Dictionary

# Copy Dictionaries
band2 = band.copy()
band2["drums"] = "Percy"
print(band)
print(band2)

band3 = dict(band)
print(band)
print(band3)

# Nested Dictionaires
member1 = {
    'name': 'Cody',
    'instrument': 'vocals'
}
member2 = {
    'name': 'Percy',
    'instrument': 'guitar'
}
band= {
    'member1': member1,
    'member2': member2
}
print(band)
print(band["member1"]["name"]) # 2 Levels deep