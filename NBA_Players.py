import requests  # Import the requests library to make HTTP requests
import csv  # Import the CSV library for handling CSV files
import time
import os.path

print("Hello and Welcome to NBA Player API\n")
time.sleep(2)
print("All player's Full name, id, position, and team will be returned and written in nba_players.csv\n")
time.sleep(2)
key = input("Please enter rapid API key for 'Free NBA' ex:*****5883emshec59*****4a73d5p11afadjsn20**********\n")
url = "https://free-nba.p.rapidapi.com/players" # The URL of the NBA players API
querystring = {"per_page": "100"}  # Parameters to be sent with the API request

headers = {
    "X-RapidAPI-Key": "",
    "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

headers.update({"X-RapidAPI-Key": key})
#response = requests.get(url , headers=headers, params=querystring)
players = []  # Initialize an empty list to store player data
next_page = True  # Starts the while loop
page = 0  # Initialize variable to iterate through pages

# While there is a next page, the loop will continue
while next_page is not None:
    querystring["page"] = page # Sets the page number in the querystring parameters
    response = requests.get(url , headers=headers, params=querystring)
    data = response.json()  # Create a variable for handling
    next_page = data["meta"]["next_page"]  # "meta" is the second key-value; "next_page" is the condition being checked

    # Extract and store player information in the 'players' list
    for player in data["data"]:
        # Joining both names and storing them in a variable
        full_name = f"{player['first_name']} {player['last_name']}"
        players.append({
            "id": player["id"],
            "position": player["position"],
            "full_name": full_name,
            # Access nested dictionary
            "team": player["team"]["full_name"]
        })
        # Move to the next page for the next iteration
    page += 1

csv_file = "nba_players.csv"
# Write player data to a CSV file

with open(csv_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "position", "full_name", "team"], extrasaction='ignore')
    writer.writeheader()  # Write the header row with column names
    writer.writerows(players) # Write the player data rows to the CSV file
# checking if file was created 
path = './nba_players.csv'
check_file = os.path.exists(path)

if check_file == True:
    time.sleep(2)
    print("\nEverything went smoothly, you should see the nba_players.csv")
else:
    time.sleep(2)
    print("\nError try again")
