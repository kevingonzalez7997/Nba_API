import requests  # Import the requests library to make HTTP requests
import csv  # Import the CSV library for handling CSV files

url = "https://free-nba.p.rapidapi.com" # The URL of the NBA players API
querystring = {"per_page": "100"}  # Parameters to be sent with the API request

headers = {
    "X-RapidAPI-Key": "4fba45883emshec591bdcb4a73d5p11afadjsn204c3ecd687d",
    "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

players = []  # Initialize an empty list to store player data
next_page = True  # Starts the while loop
page = 0  # Initialize variable to iterate through pages

# While there is a next page, the loop will continue
while next_page is not None:
    querystring["page"] = page # Sets the page number in the querystring parameters
    response = requests.get(url + "/players", headers=headers, params=querystring)
    data = response.json()  # Create a variable for handling
    next_page = data["meta"]["next_page"]  # "meta" is the second key-value; "next_page" is the condition being checked

    # Extract and store player information in the 'players' list
    for i in data["data"]:
        # Joining both names and storing in a variable
        full_name = f"{i['first_name']} {i['last_name']}"
        players.append({
            "id": i["id"],
            "position": i["position"],
            "full_name": full_name,
            # Access nested dictionary
            "team": i["team"]["full_name"]
        })
        # Move to the next page for the next iteration
    page += 1

csv_file = "nba_players.csv"
# Write player data to a CSV file

with open(csv_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "position", "full_name", "team"], extrasaction='ignore')
    writer.writeheader()  # Write the header row with column names
    writer.writerows(players) # Write the player data rows to the CSV file
