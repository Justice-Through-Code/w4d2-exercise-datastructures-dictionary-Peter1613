
'''
    Below is a dictionary consisting of details of 1 restaurant fetched from Yelp.
'''

restaurant_1 = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "state": "CA",
    "address": "375 Valencia St",
    "zip_code": "94113",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}


def explore_data():
    print(restaurant_1 ["url"])
    print(restaurant_1 ["latitude"], restaurant_1 ["longitude"])
    print(f'{restaurant_1 ["address"]}, {restaurant_1 ["city"]}, {restaurant_1 ["state"]}, {restaurant_1 ["zip_code"]}')
        
    # 1.1 TODO: Print the URL of the website of Four Barrel Coffee.

    # 1.2 TODO: Print the latitude and longitude of Four Barrel Coffee, using one print statement.

    # 1.3 TODO: Print the complete address of the Four Barrel Coffee, formatted as a string - 
    # it should include the address, city, state and the zip code, with commas between them e.g.:
    # "375 Valencia St, San Francisco, CA, 94113"

# explore_data()


def favorite_restaurant():
    # Let's ask the user for some information about their favorite restaurant

    # 2.1 TODO: Create an empty dictionary in a variable called `favorite_restaurant`

    # 2.2 TODO: Ask the user for the restaurant `name`, `address`, and their `favorite_dish`
    # Add all three of these as key value pairs in your new dictionary, ala:
    #    favorite_restaurant  = {
    #        "name": "Subway",
    #        "address" : "116th & Broadway, NY 10016",
    #        "favorite_dish" : "Chicken BLT Sandwich"
    #    }
    favorite_restaurant = {}
    
    for f in range(1):
        fav_rs_name = input("What is the name of your favorite restaurant? ")
        fav_rs_address = input("What is the address of your favorite restaurant? ")
        fav_rs_dish = input("What is your favorite dish at your favorite restaurant? ")
        
    favorite_restaurant["name"] = fav_rs_name
    favorite_restaurant["address"] = fav_rs_address
    favorite_restaurant["favorite_dish"] = fav_rs_dish
    print(favorite_restaurant)
    del favorite_restaurant["favorite_dish"]
    print(favorite_restaurant)
    favorite_restaurant["address"] = "116th & Broadway, NY 10016"
    print(favorite_restaurant["address"])
    
    # 2.3 TODO: Print out your dictionary to make sure it populated correctly

    # Oh no, the restaurant stopped serving the user's favorite dish!
    # 2.4 TODO: Remove the `favorite_dish` key/value pair from the dictionary

    # 2.5 TODO: Print out the dictionary again. This time, the dictionary 
    # should only contain a 'name' and 'address' for that restaurant

    # Looks like the restaurant is going through a lot of changes-- they moved!
    # 2.6 TODO: Update the address of the user's favorite restaurant to "116th & Broadway, NY 10016"

    # 2.7 TODO: Print out the restaurant's new address by printing the dictionary's value 
    # for the key `address`

# favorite_restaurant()


def clean_print():
    for key, value in restaurant_1.items():
        print('{}: {}'.format(key, value))
        
        
    # Peter's Note:
    # I created a for loop as written above but with print(key,":",value). 
    # My run got a space between key and colon when
    # I printed. I was stuck on this for a while before I went to stackoverflow and learned
    # the .format method. Empty brackets can be used as placeholders and .format returns the 
    # keys and values as strings.

    # It's hard to read the contents of a dictionary when we print the whole thing out.

    # 3.1 TODO: Instead, loop through each item-pair in the `restaurant_1` dictionary
    # and print out each key and value on their own line, ala:
    #      `name: Four Barrel Coffee
    #       url: https://www.yelp.com/biz/four-barrel-coffee-san-francisco`
    # etc etc

# clean_print()