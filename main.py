import requests
import os
import dotenv

dotenv.load_dotenv()

api_key = os.getenv("API_KEY")


get_puuid_api_link = "https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/"
get_rank_api_link = "https://euw1.api.riotgames.com/lol/league/v4/entries/by-puuid/"


while True:

    riot_id = input("Entrer le RiotID (q pour quitter): ")

    if riot_id == "q":
        break


    game_name = riot_id[:riot_id.find("#")]
    tag_line = riot_id[riot_id.find("#")+1:]


    raw_puuid = requests.get(f"{get_puuid_api_link}{game_name}/{tag_line}?api_key={api_key}")
    raw_puuid_json = raw_puuid.json()

    if raw_puuid.status_code == 200:
        puuid = raw_puuid_json["puuid"]
    elif raw_puuid.status_code == 404:
        print("RiotID non trouvé")
        continue
    else:
        print(f"Erreur {raw_puuid.status_code}")
        continue


    raw_rank_info = requests.get(f"{get_rank_api_link}{puuid}?api_key={api_key}")

    if raw_rank_info.status_code != 200:
        print(f"Erreur {raw_rank_info.status_code}")
        continue

    raw_rank_info_json = raw_rank_info.json()

    if len(raw_rank_info_json) == 0:
        print("Pas d'infos")
        continue

    all_rank_info = []

    for queue in raw_rank_info_json:
        rank_info = {}
        rank_info["queueType"] = queue["queueType"]
        rank_info["tier"] = queue["tier"]
        rank_info["rank"] = queue["rank"]
        rank_info["leaguePoints"] = queue["leaguePoints"]

        all_rank_info.append(rank_info)


    for queue in all_rank_info:
        print(f"En {queue['queueType']}, {riot_id} est {queue['tier']} {queue['rank']} avec {queue['leaguePoints']} LP")
    
    input()