import bs4 as bs
import urllib.request  # request istemek oluyomuş url=adres adreskütüphanesinden bişi istiyoruz
kaynak=urllib.request.urlopen("https://www.gittigidiyor.com/").read()  #değişken belirledik adreskütüphanesinden istediğimizi açmasını ve okumasını istiyoruz
sayfa=bs.BeautifulSoup(kaynak,"lxml")   #bi değişken daha atadık xlml kaynaklı bişiler dedi
#print(sayfa.findAll("p"))  #findall komutu burda sayfanın içindeki her şeyi getiriyor kısıtlama koyduk p etiketi ile olanları aldık sadece paragraf olanları yani
#for div in sayfa.findAll("div"):
#print(sayfa.get_text()) #sayfadaki tüm textleri çekiyormuş.
sonuc=sayfa.findAll("p",{"class":"discount-price"})
print(sonuc)
toplam=0
for fiyat in sonuc:
    
    fiyat=fiyat.string    
    fiyat=fiyat.replace("TL","")    
    fiyat="".join(fiyat.split())
    fiyat=fiyat.replace(".","")
    fiyat=fiyat[:-3]
    fiyat=int(fiyat)
    print("Fiyat:",fiyat)
    toplam=toplam+fiyat
ortalama=toplam/len(sonuc)
print("Toplam:",toplam)
print("Ortalama:",ortalama) 


öünümüzdeki hafta düşünün diyo bi web sitesinden ne alabiliriz die