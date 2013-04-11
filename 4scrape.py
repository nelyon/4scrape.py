import sys, os, re, urllib2, urlparse
try: 
  folder = sys.argv[2]
	try: os.makedirs(folder)
	except: pass
except IndexError: folder = "./"
def scrape(url, dest):
	for cimg in re.findall('a class="fileThumb".*?href="(.*?)"', urllib2.urlopen(url).read()):
		out = open(dest+"/"+os.path.basename(urlparse.urlsplit(cimg)[2]), "w+")
		out.write(urllib2.urlopen("http:" + cimg).read())
	out.close()
try: scrape(sys.argv[1], folder)
except:	print('- 4scrape.py -\n\nUsage: 4scrape.py [url] [directory] ')
