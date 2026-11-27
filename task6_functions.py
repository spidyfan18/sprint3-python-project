def calculate_total_sales(game):
    return game[NA_SALES] + game[EU_SALES] + game[JP_SALES]
print(calculate_total_sales(video_game_sales[0]))  

def filter_by_genre(data,genre ='Platform'):
    result = []
    for p_game in data:
        if p_game[GENRE] == genre:
            result.append(p_game)
    return result
platform_games = filter_by_genre(video_game_sales)
sports_game = filter_by_genre(video_game_sales, 'Sports')
print(len(platform_games))
print(len(sports_game))

def get_summary(game):
    return f"{game[NAME]} ({game[YEAR]}) - {game[GENRE]} - ${game[GLOBAL_SALES]}M"
for g_s in video_game_sales:
    print(g_s)
