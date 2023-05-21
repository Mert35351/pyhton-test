
import requests
from bs4 import BeautifulSoup

link_href = []
son_href = ""

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
                    link_tespit.append({"link":href_url,
                                       "time":x})


    if link_tespit:

        if link_tespit[0]['link'] != son_href:
            print("Merhaba",link_tespit[0]['link'])

            print(link_tespit[0]['link'])

            son_href = link_tespit[0]['link']












































