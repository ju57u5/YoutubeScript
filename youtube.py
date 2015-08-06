import time
import datetime
import cookielib
import mechanize
import sys
import urlparse
import os
import argparse
import re

def openUrl(url):
	LoginHeader = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)"}
	req = mechanize.Request(url)
	response = mechanize.urlopen(req)
	html = response.read()
	return html

def unixtime():
	then = datetime.datetime.now()
	return int(time.mktime(then.timetuple())*1e3 + then.microsecond/1e3)

def stringbetween(string,startstr,endstr):
	start = string.find(startstr)
	end = string.find(endstr,start+len(startstr))
	return string[start+len(startstr):end]

def downloadvideo(url,name,vformat):
	html = openUrl('http://convert2mp3.net/c-'+vformat+'.php?url='+url)
	convertbefehl = stringbetween(html,'convert(',');')

	idstart=convertbefehl.find('"')
	idend=convertbefehl.find('"',idstart+1)
	keystart=convertbefehl.find('"',idend+1)
	keyend=convertbefehl.find('"',keystart+1)
	csstart=convertbefehl.find('"',keyend+1)
	csend=convertbefehl.find('"',csstart+1)

	vid=convertbefehl[idstart+1:idend]
	key=convertbefehl[keystart+1:keyend]
	cs=convertbefehl[csstart+1:csend]

	convertframe=stringbetween(html, '"convertFrame" src="', '"')
	openUrl(convertframe)

	html2 = '1'
	while not "3" in html2 :
		html2 = openUrl('http://convert2mp3.net/status.php?id='+vid+'&key='+key+'&cs='+cs+'&time='+str(unixtime()))
		print('Converting...')
		time.sleep(1)
	print 'Downloading...'
	downloadurl='http://cdl'+cs+'.convert2mp3.net/download.php?id='+vid+'&key='+key

	split = urlparse.urlsplit(downloadurl)
	if not os.path.exists(os.path.dirname(os.path.realpath(__file__))+ "\\download"):
	    os.makedirs(os.path.dirname(os.path.realpath(__file__))+ "\\download")
	filename = os.path.dirname(os.path.realpath(__file__))+ "\\download\\" + name +"."+vformat
	mechanize.urlretrieve(downloadurl, filename)
	return

def getVideoID(url):
	url_data = urlparse.urlparse(url)
	query = urlparse.parse_qs(url_data.query)
	if not "v" in query:
		print 'Video Url is not valid!'
		sys.exit(1)
	video = query["v"][0]
	return video
def getPlaylistID(url):
	url_data = urlparse.urlparse(url)
	query = urlparse.parse_qs(url_data.query)
	plid = query["list"][0]
	return plid

def unique(a):
    seen = set()
    return [seen.add(x) or x for x in a if x not in seen]

def getPlaylistVideos(url):
	html = openUrl('http://www.youtube.com/playlist?list='+getPlaylistID(url))
	links = re.findall('watch\?v=.{16}',html.rstrip('\n'))
	for i,entry in enumerate(links):
		links[i] = 'http://www.youtube.com/watch?v=' + stringbetween(entry,'watch?v=','&amp;')
	if not links:
		print 'Couldnt read Playlist. Try again!'
		sys.exit(1)
	return unique(links)

def checkFormats(parser,x):
	formats = ['mp3','m4a','acc','flac','ogg','wma','mp4','avi','wmv','3gp']
	if not (x in formats):
		parser.error("Format must be: "+' '.join(formats))
	else :
		return x

def dlplaylist(args):
	plvideos = getPlaylistVideos(args.videourl)
	prefix = ''
	if args.name == 'none':
		prefix = getPlaylistID(args.videourl)
	else :
		prefix = args.name

	for i,entry in enumerate(plvideos):
		if (i+1>=args.start and i+1<=args.end) :
			downloadvideo(entry, str(i+args.startno)+" "+prefix, args.format)
	return

aparser = argparse.ArgumentParser(description='Download Youtube Videos and Playlists.')
aparser.add_argument('-f', '--format', type=lambda x: checkFormats(aparser,x), dest='format', action="store", default="mp3", help='Format of the downloaded Videos(see convert2mp3.net)')
aparser.add_argument('-n', '--name', dest='name', action="store", default="none", help='Name of the downloaded Video without Fileext.')
aparser.add_argument('videourl', metavar='url', action="store", help='URL of the Video or Playlist')
aparser.add_argument('-pl', '--playlist', dest='playlist', action="store_true", help='Downloads Playlist')
aparser.add_argument('-no', '--startno', dest='startno', action="store", type=int, default=1, help='Starting Number of Naming, if downloading Playlist')
aparser.add_argument('-s', '--start', dest='start', action="store", type=int, default=1, help='Starting Number, if downloading Playlist')
aparser.add_argument('-e', '--end', dest='end', action="store", type=int, default=1000, help='Ending Number, if downloading Playlist')

args = aparser.parse_args()

if args.playlist:
	dlplaylist(args)
elif (args.name == 'none'):
	downloadvideo(args.videourl,getVideoID(args.videourl),args.format)
else:
	downloadvideo(args.videourl,args.name,args.format)
