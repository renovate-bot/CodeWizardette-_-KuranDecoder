# بسم الله الرحمن الرحيم

# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from collections import Counter, defaultdict
from nltk import ngrams
import nltk
from nltk.corpus import stopwords

def metin_temizle(metin):
    temiz_metin = metin.replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("!", "").replace("?", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("'", "").replace('"', "").replace("-", "").replace("_", "").replace("/", "").replace("\\", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "").replace("+", "").replace("=", "").replace("|", "").replace("~", "").replace("`", "").replace("<", "").replace(">", "")
    temiz_metin = temiz_metin.lower()
    return temiz_metin

def kelime_frekansi(metin):
    kelimeler = metin.split()
    frekanslar = defaultdict(int)
    for kelime in kelimeler:
        frekanslar[kelime] += 1
    return frekanslar

def kelime_uzunlugu_histogrami(metin):
    kelimeler = metin.split()
    uzunluklar = [len(kelime) for kelime in kelimeler]
    plt.hist(uzunluklar, bins=range(min(uzunluklar), max(uzunluklar) + 2, 1), edgecolor='black')
    plt.xlabel('Kelime Uzunluğu')
    plt.ylabel('Frekans')
    plt.title('Kelime Uzunluğu Histogramı')
    plt.show()

def kelime_freksansi_grafik(metin, en_cok=10):
    frekanslar = kelime_frekansi(metin)
    en_cok_kelimeler = Counter(frekanslar).most_common(en_cok)
    kelimeler, frekanslar = zip(*en_cok_kelimeler)
    plt.bar(kelimeler, frekanslar)
    plt.xlabel('Kelime')
    plt.ylabel('Frekans')
    plt.title(f'En Sık {en_cok} Kelime')
    plt.xticks(rotation=45)
    plt.show()

with open("kuran.txt", "r", encoding="utf-8") as file:
    kuran_metni = file.read()

temiz_metin = metin_temizle(kuran_metni)

# Stop kelimeleri çıkar
nltk.download('stopwords')
stop_kelimeler = set(stopwords.words('arabic'))
kelimeler = temiz_metin.split()
kelimeler_filtrli = [kelime for kelime in kelimeler if kelime not in stop_kelimeler]

kelime_uzunlugu_histogrami(kelimeler_filtrli)
frekanslar = kelime_frekansi(kelimeler_filtrli)
kelime_freksansi_grafik(frekanslar)

# Bigram frekans analizi
bigramler = ngrams(kelimeler_filtrli, 2)
bigram_frekanslar = defaultdict(int)
for bigram in bigramler:
    bigram_frekanslar[bigram] += 1

kelime_freksansi_grafik(bigram_frekanslar, en_cok=10)
temiz_metin = metin_temizle(kuran_metni)
kelime_uzunlugu_histogrami(temiz_metin)
kelime_freksansi_grafik(temiz_metin)

# Grafik gösterme yerine kaydetme
plt.savefig("kelime_uzunlugu_histogrami.png")
plt.savefig("bigramler.png")
plt.show()
