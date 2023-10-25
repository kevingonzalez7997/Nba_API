# NBA Player API Data Retrieval Python
Kevin Gonzalez

## Purpuse

This Python script is designed to fetch data from the "Free NBA" API, specifically player information, and save it to a CSV file. The data includes each player's full name, ID, position, and team. It also checks to confirm if the file has been created.

## Prerequisites

- Before running this script, you need to obtain an API key from the "Free NBA" API. You will be prompted to input your API key when running the script
- `pip install requests` to be able to make an API call

## Script Explanation

The script works as follows:

1. It imports necessary libraries, including `requests` for making API requests and `csv` for handling CSV files.

2. It prints a welcome message and instructions for what the script will do.

3. You will be prompted to enter your Free NBA API key, which is used for authentication.

4. The script makes HTTP requests to the API, fetching player data in batches of 100 players per page. It iterates through pages until there are no more pages left.

5. Player data is extracted and stored in a list.

6. The collected player data is written to a CSV file named `nba_players.csv` with columns for ID, position, full name, and team.

7. Finally, the script checks if the file was successfully created and provides appropriate feedback.
