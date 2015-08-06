# YoutubeScript
Commandline Utility for convert2mp3.net

# Usage
ytdl.py [-h] [-f FORMAT] [-n NAME] [-pl] [-no STARTNO] [-s START] [-e END] url

Download Youtube Videos and Playlists over convert2mp3.net.

### positional arguments:<br>
Argument|Description
|-------------------------------|--------------------------------------------------------
|  url                           | URL of the Video or Playlist

### optional arguments:<br>
|  Flag							|  Description
|  -----------------------------|------------------------------------------------------ 
|  -h, --help                    |  show this help message and exit
|  -f FORMAT, --format FORMAT    |  format of the downloaded videos(see convert2mp3.net)
|  -n NAME, --name NAME          |  name of the downloaded video without fileextension
|  -pl, --playlist               |  downloads playlist
|  -no STARTNO, --startno STARTNO|  starting number of naming, if downloading Playlist
|  -s START, --start START       |  starting number, if downloading Playlist
|  -e END, --end END             |  ending number, if downloading Playlist
