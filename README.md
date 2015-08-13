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
|  -no STARTNO, --startno STARTNO|  starting number of naming, if downloading playlist
|  -s START, --start START       |  starting number, if downloading playlist
|  -e END, --end END             |  ending number, if downloading playlist


#Examples
```
ytdl.py -no 24 -n pietcast -s 5 -e 8 -pl https://www.youtube.com/playlist?list=PL5JK9SjdCJp_oIlCBbnANeOvT8yuCxBbu
```
Downloads episodes 5 to 8 from "PietCast" and names them "<24+playlist video index> pietcast.mp3".

```
ytdl.py -f mp4 -n ytrewind2008 https://www.youtube.com/watch?v=zKx2B8WCQuw
```
Downloads the "YoutubeRewind 2008" and names it ytrewind2008.mp4 


All downloads will be placed at {ScriptDir}/download

#Download
This script is available as Windows application or source at the [releases page](https://github.com/ju57u5/YoutubeScript/releases).
