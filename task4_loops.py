for game_sales in video_game_sales:
    if game_sales[GLOBAL_SALES]> 25:
        print (game_sales[GLOBAL_SALES],game_sales[NAME])

pre_2000_count = 0
    
for game_count in video_game_sales:
    if game_count[YEAR]< 2000:
        pre_2000_count = pre_2000_count + 1
print(pre_2000_count)

NA_sales = 0
JP_sales = 0
for game_sales in video_game_sales:
        NA_sales = NA_sales + game_sales[NA_SALES]
        JP_sales = JP_sales + game_sales[JP_SALES]
print(f"total North america sales:{NA_sales}")
print(f"total JP sales: {JP_sales}")
if NA_sales > JP_sales:print("NA Higher")
elif JP_sales > NA_sales:print("JP Higher")
else: print("none")

nintendo_games = []
for n_games in video_game_sales:
    if n_games[PUBLISHER]=="Nintendo":
        nintendo_games.append(n_games[NAME])
print(nintendo_games)
print(len(nintendo_games))
