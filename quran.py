import requests
from bs4 import BeautifulSoup
def al(pesan,ke=0):
	try:
		ke = int(ke)
		url = "https://litequran.net/"+pesan
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
		source=requests.get(url, headers=headers).text
		soup = BeautifulSoup(source, 'html.parser')
		ayat = soup.find_all("span","ayat")
		bacaan = soup.find_all("span","bacaan")
		arti = soup.find_all("span","arti")
		hasil=""
		if ke==0:
			if len(ayat)>9:
				hasil += pesan + " Ayat 1-10\n\n"
				for x in range(10):
					hasil += ayat[x].text +"\n\n"
					hasil += bacaan[x].text + "\n\n"
					hasil += arti[x].text + "\n\n\n\n"
			else:
				hasil += pesan + " Ayat 1-"+str(len(ayat))+"\n\n"
				for x in range(len(ayat)):
					hasil += ayat[x].text +"\n\n"
					hasil += bacaan[x].text + "\n\n"
					hasil += arti[x].text + "\n\n\n\n"
		elif 0<ke<=len(ayat):
			hasil += pesan + " Ayat "+str(ke)+"\n\n"
			hasil += ayat[ke-1].text + "\n\n"
			hasil += bacaan[ke-1].text + "\n\n"
			hasil += arti[ke-1].text
		else:
			hasil += "Ayat ke "+str(ke)+" tidak ditemukan."
	except:
		hasil = "Ayat tidak ditemukan."
	return hasil