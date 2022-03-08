# Dictionary

# Dictionary lets you store data in key-value pairs
# Each item must be associated with a unique key
# The key is used to access the particular value in the dictionary
# While the keys must be unique, the values can be redundant
# The order of keys and values is undefined in a dictionary

ssn_name_pairs = dict()

# Alternatively ssn_name_pairs = {}

# Defining dictionary key value pairs - dictionary[key] = value

# ssn_name_pairs["123-456-789"] = "John Appleseed"
# ssn_name_pairs["000-000-002"] = "Dwight Schrute"
# ssn_name_pairs["000-000-005"] = "Pam Beesly"

# Alternate method

ssn_name_pairs = {
    "123-456-789":"John Appleseed", 
    "000-000-002":"Dwight Schrute", 
    "000-000-005":"Pam Beesly"
        }
print(ssn_name_pairs)
print(ssn_name_pairs["123-456-789"])

# Add new key-value pair
