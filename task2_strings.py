messy_names = ['  Wii Sports  ', 'TETRIS', '  mario kart WII']
game_name = video_game_sales[4][NAME]
print(game_name[0:7])

for names in messy_names:
    print(names.strip().lower())


print(f"#1 Best Seller: {video_game_sales[0][NAME]} ({video_game_sales[0][YEAR]}) - ${video_game_sales[0][GLOBAL_SALES]}M global sales")

