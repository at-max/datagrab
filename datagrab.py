import requests
from bs4 import BeautifulSoup
import os
import tkinter as tk

def onayla():
    metin = metin_kutusu.get()

    kelimeler = metin.split()
    flip_cümle = "_".join(kelimeler)

    # web sayfasından veriyi al
    response = requests.get("https://tr.wikipedia.org/wiki/" + flip_cümle)

    # check if response is successful before parsing HTML
    if response.status_code == 200:
        # BeautifulSoup nesnesi oluştur
        soup = BeautifulSoup(response.content, "html.parser")

        # tüm başlıkları seç
        headings = soup.find_all("p")

        # construct output file path
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        output_file = os.path.join(output_dir, metin + ".txt")

        # write content of each paragraph to file
        with open(output_file, "w", encoding="utf-8") as f:
            for heading in headings:
                f.write(heading.text.strip())

            f.write("\n\nDatagraph ile yazıldı\n")
            
pencere = tk.Tk()
pencere.geometry("250x75")
pencere.title("DataGrab v1")

etiket = tk.Label(pencere, text="DataGrab")
etiket.pack()

metin_kutusu = tk.Entry(pencere)
metin_kutusu.pack()


onay_butonu = tk.Button(pencere, text="Onayla", command=onayla)
onay_butonu.pack()

pencere.mainloop()
