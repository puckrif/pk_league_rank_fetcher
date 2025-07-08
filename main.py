import player_rank

while True:

    riot_id = input("Entrer le RiotID (q pour quitter): ")

    if riot_id == "q":
        break

    ranks = player_rank.get_ranks(riot_id)

    if ranks["ranks"] == None:
        if ranks["puuid_code"] != None:
            print(f"Erreur account-v1 {ranks['puuid_code']}")
        else :
            print(f"Erreur league-v4 {ranks['ranks_code']}")
    else :
        print(f"{riot_id} :")
        print(ranks['ranks'].__str__())

    
    input()