import requests
import csv

url = "https://free-nba.p.rapidapi.com/players"
querystring = {"per_page":"100"}

headers = {
	"X-RapidAPI-Key": "4fba45883emshec591bdcb4a73d5p11afadjsn204c3ecd687d",
	"X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

players = []
next_page = True
page = 0 

while(next_page != None ): 
    querystring["page"] = str(page)
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    next_page = data["meta"]["next_page"]
     
    for i in data["data"]:
        full_name =f"{i['first_name']} {i['last_name']}"
        players.append({
            "id":i["id"],
            "position":i["position"],
            "full_name": full_name,
            "team":i["team"]["full_name"]

        }) 
    page += 1   

csv_file = "nba_players.csv"
with open(csv_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "position", "full_name","team"], extrasaction='ignore')
    writer.writeheader()
    writer.writerows(players)
