"""
klavyeden girilen 5 sayıyı bir listeye atarak bunların karelerinden 20 cıktıgında ortaya cıkan sonuca göre sıralayan
ve listeyi buna göre yazdıran programı yazın.
"""

liste =[]
for i in range (0,5):
  liste.append(int(input()))


def siralama_fonksiyonu(a):
  return a*a-20


liste.sort(key=siralama_fonksiyonu)
print(liste)
