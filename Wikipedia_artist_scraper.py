


from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

artist_url = r'https://en.wikipedia.org/wiki/List_of_hip_hop_musicians' #includes names of all individual hip hop artists
group_url = r'https://en.wikipedia.org/wiki/List_of_hip_hop_groups' #includes names of all hip hop groups




def get_all_artists(url):
    req = Request(url,headers = {'User-Agent': 'Mozilla/5.0'})
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")
    
    artist_soup = soup.findAll('div',attrs={'class':'div-col columns column-width'}) #all artists names included in these divs
    names=[]
    for group in artist_soup:
        name_objs = group.findAll('a') #all names are hyperlinks within our divs
        for obj in name_objs:
            try:
                name = obj['title'] #Title returns just the text associated with the name
                names.append(name)
            except:
                pass
    
    #Remove (rapper) from some names, strip whitespace
    #Remove citation hyperlinks
    names = [name.split('(')[0].strip() for name in names if name != 'Wikipedia:Citation needed'] 
    return names




individuals = get_all_artists(artist_url)

groups = get_all_artists(group_url)




with open('hip_hop_artists.txt','w', encoding="utf-8") as outfile:
    for name in individuals:
        outfile.write(name + '\n')




with open('hip_hop_groups.txt','w', encoding="utf-8") as outfile:
    for name in groups:
        outfile.write(name + '\n')

