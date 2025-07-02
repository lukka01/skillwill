fruits = ["apple", "banana", "pear"]
print("Original list:", fruits)
fruits.append("peach")
print("After appending:", fruits)
fruits.remove("banana")
print("After removing 'banana':", fruits)
fruits.reverse()
print("Reversed list:", fruits)
print("Length of the list:", len(fruits))

person = {
    "name": "Luka",
    "age": 19,
    "city": "Tbilisi"
}
print("Original dictionary:", person)
person["hobby"] = "boxing"
print("After adding hobby:", person)
person["age"] = 21
print("After changing age:", person)
print("City:", person.get("city"))
person.pop("hobby")
print("After removing hobby:", person)

coordinates = (41.7151, 44.8271)
print("Original tuple:", coordinates)
print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])
lat, lon = coordinates
print("Unpacked:", "lat =", lat, ", lon =", lon)
print("Length of the tuple:", len(coordinates))
