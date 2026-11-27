sales_by_genre = {}
for n_genre in video_game_sales:
    genre = n_genre[GENRE]
    sales = n_genre[GLOBAL_SALES]
    if genre in sales_by_genre:
        sales_by_genre[genre]= sales_by_genre[genre]+ sales
    else:
         sales_by_genre[genre] = sales
print(sales_by_genre)

games_per_publisher = {}
for n_publisher in video_game_sales:
    pub = n_publisher[PUBLISHER]
    if pub in games_per_publisher:
        games_per_publisher[pub]=games_per_publisher[pub]+1
    else:
          games_per_publisher[pub] = 1      
print(games_per_publisher)  

top_game = {'name':video_game_sales[0][NAME],'year':video_game_sales[0][YEAR],'genre': video_game_sales[0][GENRE],'publisher': video_game_sales[0][PUBLISHER],'global_sales':video_game_sales[0][GLOBAL_SALES]}


for key, sale in top_game.items():
    print (key,sale)
