import appscript
import urllib.parse
import webbrowser

it = appscript.app("iTunes")

song = it.current_track.name.get()
artist = it.current_track.artist.get()

webbrowser.open("https://twitter.com/intent/tweet?text=NowPlaying:%20" + urllib.parse.quote(song) + "%20(" + urllib.parse.quote(artist) + ")")