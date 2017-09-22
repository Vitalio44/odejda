import requests
from bs4 import BeautifulSoup
from goods.models import Goods


def func1():
    # Парсим раздел Женская одежда
    o_j_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/gallery/KATALOG/Odezhda-zhenskaya/"
    url_page1 = o_j_url + "1-28-63.html"
    url_page2 = o_j_url + "29-28-63.html"
    url_page3 = o_j_url + "57-28-63.html"
    url_page4 = o_j_url + "85-28-63.html"
    url_page5 = o_j_url + "113-28-63.html"

    r1 = requests.get(url_page1)
    r2 = requests.get(url_page2)
    r3 = requests.get(url_page3)
    r4 = requests.get(url_page4)
    r5 = requests.get(url_page5)

    soup1 = BeautifulSoup(r1.content, 'html.parser')
    g_data1 = soup1.find_all("div", {"class": "img"})

    soup2 = BeautifulSoup(r2.content, 'html.parser')
    g_data2 = soup2.find_all("div", {"class": "img"})

    soup3 = BeautifulSoup(r3.content, 'html.parser')
    g_data3 = soup3.find_all("div", {"class": "img"})

    soup4 = BeautifulSoup(r4.content, 'html.parser')
    g_data4 = soup4.find_all("div", {"class": "img"})

    soup5 = BeautifulSoup(r5.content, 'html.parser')
    g_data5 = soup5.find_all("div", {"class": "img"})

    Goods.objects.all().delete()

    # Сохраняем в модель товары данной категории
    for item in g_data1:
        img_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/" + str(item.contents[1].get("href"))
        price = str(item.contents[3])
        good = Goods(goods_category_id=1, img_url=img_url, price=price)
        good.save()

    for item in g_data2:
        img_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/" + str(item.contents[1].get("href"))
        price = str(item.contents[3])
        good = Goods(goods_category_id=1, img_url=img_url, price=price)
        good.save()

    for item in g_data3:
        img_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/" + str(item.contents[1].get("href"))
        price = str(item.contents[3])
        good = Goods(goods_category_id=1, img_url=img_url, price=price)
        good.save()

    for item in g_data4:
        img_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/" + str(item.contents[1].get("href"))
        price = str(item.contents[3])
        good = Goods(goods_category_id=1, img_url=img_url, price=price)
        good.save()

    for item in g_data5:
        img_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/" + str(item.contents[1].get("href"))
        price = str(item.contents[3])
        good = Goods(goods_category_id=1, img_url=img_url, price=price)
        good.save()

    # Парсим раздел Мужская одежда
    o_m_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/gallery/KATALOG/Odezhda-muzhskaya/"
    o_m_url_page1 = o_m_url + "1-28-64.html"
    o_m_url_page2 = o_m_url + "29-28-64.html"
    o_m_url_page3 = o_m_url + "57-28-64.html"

    o_m_r1 = requests.get(o_m_url_page1)
    o_m_r2 = requests.get(o_m_url_page2)
    o_m_r3 = requests.get(o_m_url_page3)

    o_m_soup1 = BeautifulSoup(o_m_r1.content)
    o_m_g_data1 = o_m_soup1.find_all("div", {"class": "img"})

    o_m_soup2 = BeautifulSoup(o_m_r2.content)
    o_m_g_data2 = o_m_soup2.find_all("div", {"class": "img"})

    o_m_soup3 = BeautifulSoup(o_m_r3.content)
    o_m_g_data3 = o_m_soup3.find_all("div", {"class": "img"})

    # Сохраняем в модель товары данной категории
    for item in o_m_g_data1:
        img_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/" + str(item.contents[1].get("href"))
        price = str(item.contents[3])
        good = Goods(goods_category_id=2, img_url=img_url, price=price)
        good.save()

    for item in o_m_g_data2:
        img_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/" + str(item.contents[1].get("href"))
        price = str(item.contents[3])
        good = Goods(goods_category_id=2, img_url=img_url, price=price)
        good.save()

    for item in o_m_g_data3:
        img_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/" + str(item.contents[1].get("href"))
        price = str(item.contents[3])
        good = Goods(goods_category_id=2, img_url=img_url, price=price)
        good.save()

    # Парсим раздел Детская одежда
    o_d_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/gallery/KATALOG/Odezhda-detskaya/"
    o_d_url_page1 = o_d_url + "1-28-65.html"
    o_d_url_page2 = o_d_url + "29-28-65.html"
    o_d_url_page3 = o_d_url + "57-28-65.html"
    o_d_url_page4 = o_d_url + "85-28-65.html"
    o_d_url_page5 = o_d_url + "113-28-65.html"

    o_d_r1 = requests.get(o_d_url_page1)
    o_d_r2 = requests.get(o_d_url_page2)
    o_d_r3 = requests.get(o_d_url_page3)
    o_d_r4 = requests.get(o_d_url_page4)
    o_d_r5 = requests.get(o_d_url_page5)

    o_d_soup1 = BeautifulSoup(o_d_r1.content)
    o_d_g_data1 = o_d_soup1.find_all("div", {"class": "img"})

    o_d_soup2 = BeautifulSoup(o_d_r2.content)
    o_d_g_data2 = o_d_soup2.find_all("div", {"class": "img"})

    o_d_soup3 = BeautifulSoup(o_d_r3.content)
    o_d_g_data3 = o_d_soup3.find_all("div", {"class": "img"})

    o_d_soup4 = BeautifulSoup(o_d_r4.content)
    o_d_g_data4 = o_d_soup4.find_all("div", {"class": "img"})

    o_d_soup5 = BeautifulSoup(o_d_r5.content)
    o_d_g_data5 = o_d_soup5.find_all("div", {"class": "img"})

    # Сохраняем в модель товары данной категории
    for item in o_d_g_data1:
        img_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/" + str(item.contents[1].get("href"))
        price = str(item.contents[3])
        good = Goods(goods_category_id=3, img_url=img_url, price=price)
        good.save()

    for item in o_d_g_data2:
        img_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/" + str(item.contents[1].get("href"))
        price = str(item.contents[3])
        good = Goods(goods_category_id=3, img_url=img_url, price=price)
        good.save()

    for item in o_d_g_data3:
        img_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/" + str(item.contents[1].get("href"))
        price = str(item.contents[3])
        good = Goods(goods_category_id=3, img_url=img_url, price=price)
        good.save()

    for item in o_d_g_data4:
        img_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/" + str(item.contents[1].get("href"))
        price = str(item.contents[3])
        good = Goods(goods_category_id=3, img_url=img_url, price=price)
        good.save()

    for item in o_d_g_data5:
        img_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/" + str(item.contents[1].get("href"))
        price = str(item.contents[3])
        good = Goods(goods_category_id=3, img_url=img_url, price=price)
        good.save()

    # Парсим раздел Одежда для школы
    o_sh_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/gallery/KATALOG/odezhda-dlya-shkoly/"
    o_sh_url_page1 = o_sh_url + "1-28-100.html"
    o_sh_url_page2 = o_sh_url + "29-28-100.html"
    o_sh_url_page3 = o_sh_url + "57-28-100.html"

    o_sh_r1 = requests.get(o_sh_url_page1)
    o_sh_r2 = requests.get(o_sh_url_page2)
    o_sh_r3 = requests.get(o_sh_url_page3)

    o_sh_soup1 = BeautifulSoup(o_sh_r1.content)
    o_sh_g_data1 = o_sh_soup1.find_all("div", {"class": "img"})

    o_sh_soup2 = BeautifulSoup(o_sh_r2.content)
    o_sh_g_data2 = o_sh_soup2.find_all("div", {"class": "img"})

    o_sh_soup3 = BeautifulSoup(o_sh_r3.content)
    o_sh_g_data3 = o_sh_soup3.find_all("div", {"class": "img"})

    # Сохраняем в модель товары данной категории
    for item in o_sh_g_data1:
        img_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/" + str(item.contents[1].get("href"))
        price = str(item.contents[3])
        good = Goods(goods_category_id=4, img_url=img_url, price=price)
        good.save()

    for item in o_sh_g_data2:
        img_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/" + str(item.contents[1].get("href"))
        price = str(item.contents[3])
        good = Goods(goods_category_id=4, img_url=img_url, price=price)
        good.save()

    for item in o_sh_g_data3:
        img_url = "http://xn--80aaaefjafck3czapfd6c0a7n.xn--p1ai/" + str(item.contents[1].get("href"))
        price = str(item.contents[3])
        good = Goods(goods_category_id=4, img_url=img_url, price=price)
        good.save()
