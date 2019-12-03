import bs4 as bs
import urllib.request  # request istemek oluyomuş url=adres adreskütüphanesinden bişi istiyoruz
kaynak=urllib.request.urlopen("https://twitter.com/login?lang=tr").read()  #değişken belirledik adreskütüphanesinden istediğimizi açmasını ve okumasını istiyoruz
sayfa=bs.BeautifulSoup(kaynak,"lxml")   #bi değişken daha atadık xlml kaynaklı bişiler dedi
print(sayfa.findAll("p"))  #findall komutu burda sayfanın içindeki her şeyi getiriyor kısıtlama koyduk p etiketi ile olanları aldık sadece paragraf olanları yani
