fav_games = (
    "Last guardian",
    "Bloodborne",
    "Armoured Core 6"
)
fav_music = (
    "Dragonsong",
    "Zanarkand",
    "Apocolypsis Noctis"
)
fav_things = {
    "games":fav_games,
    "music":fav_music
}
for key,value in fav_things.items():
    print("{}:{}".format(key, value))
#just using string formatting