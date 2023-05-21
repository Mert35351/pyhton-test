import openai
import requests
from bs4 import BeautifulSoup


# GPT-3.5 modelini ve API anahtarınızı belirtin
model = "gpt-3.5-turbo"
api_key = 

# OpenAI API'sine bağlanın
openai.api_key = api_key

# ChatGPT'yi kullanarak bir metin girişi ve modelin yanıtını almak için bir fonksiyon tanımlayın


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
    p_dict = []
    h1_dict = []

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
            print(link_tespit[0]['link'])
            url_href = "https://www.bbc.com"f"{link_tespit[0]['link']}"""
            url_r = requests.get(url_href)
            url_source = url_r.text
            url_soup = BeautifulSoup(url_source,"html.parser")
            h1_list = url_soup.find("h1")
            p_list = url_soup.find_all("p")
            img = url_soup.find("img")
            img_href = img.get('src')
            img_r = requests.get(img_href)

            for h1 in h1_list:
                h1_text = h1.text
                h1_dict.append(h1_text)

            for p in range(5):
                p_text = p_list[p].text
                p_dict.append(p_text)

            if img_r.status_code == 200:

                with open("image.jpg","wb") as file:
                    file.write(img_r.content)


                def get_chat_response(prompt):
                    response = openai.ChatCompletion.create(
                        model=model,
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    return response.choices[0].message.content.strip()

                    # Kullanıcıdan giriş alarak modelin yanıtını alın

                user_input = "ingilizce kısa özet".join([str(h1_dict), " ".join(str(p_dict))])
                response = get_chat_response(user_input)


                    # "response" çıktısını tekrar sormak için
                user_input = "türkçe kısa özetini çıkar"f"{response}"""
                response = get_chat_response(user_input)


                # "response" çıktısını tekrar sormak için
                user_input = "13 kelimelik kısa özet habere düşür ve hastag ekle!"f"{response}"""
                response = get_chat_response(user_input)



                def post_to_facebook_page(page_access_token, page_id, message, image_path):
                    api_endpoint = f"https://graph.facebook.com/v14.0/{page_id}/photos"
                    headers = {
                        "Authorization": f"Bearer {page_access_token}"
                    }
                    payload = {
                        "message": message
                    }
                    files = {
                        "source": open(image_path, "rb")
                    }

                    response = requests.post(api_endpoint, headers=headers, data=payload, files=files)
                    if response.status_code == 200:
                        print("Paylaşım başarıyla yapıldı.")
                    else:
                        print("Paylaşım yapılamadı. Hata kodu:", response.status_code)


                # Sayfa erişim anahtarını, sayfa kimliğini, paylaşım mesajını ve resim yolunu girin
                page_access_token = 
                page_id = 
                message = response
                image_path = "root/pyhton/image.jpg"

                # Sayfa paylaşımını gerçekleştirin
                post_to_facebook_page(page_access_token, page_id, message, image_path)






            else:

                print("böyle bir link bulunamadı!")








            son_href = link_tespit[0]['link']













































