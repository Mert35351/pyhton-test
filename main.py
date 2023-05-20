
import requests
from bs4 import BeautifulSoup
import time as t
import openai





sayi = 0
while True:

    ## ilk sorgu ##
    url = "https://www.bbc.com/news/world"
    r = requests.get(url)
    text = r.text
    soup = BeautifulSoup(text, "html.parser")
    divs = soup.find_all("div")
    #son
    link = []
    link_tespit = []

    sayi += 1
    print(sayi)

    # link tespiti içi div sorgusu
    for div in divs:
        time_elements = div.find_all("time",{"class":"gs-o-bullet__text"})
        href_elements = div.find_all("a",{"class":"gs-c-promo-heading"})
        # link tespiti başarılı olursa ekrana yazar
        for time, href in zip(time_elements, href_elements):

            x= time['data-datetime']
            href_url = href['href']
            link.append({"link":href_url,"time":x})


            if x == "1m":
                if href_url not in link_tespit:
                    link_tespit.append(href_url)
                    print("Eşleşme tamamlandı",href_url)


    t.sleep(10)






























