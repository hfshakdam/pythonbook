playlist = ["Backbone","Closer","Silvera"]
playlist.append("Flying Whales")
playlist.remove("Closer")
playlist.sort()
clean_playlist = ', '.join(playlist) #removes the brackets and apostophes
#by joining the list into a single, long string. Replacing gaps with whatever i choose
#I chose to use ', '

print(clean_playlist)