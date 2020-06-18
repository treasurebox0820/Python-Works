"""
このモジュールを実行する前に、必ずtext_fileというディレクトリを同じディレクトリに作成してから実行してください。
text_fileディレクトリにテキストデータは生成されます。
"""

import requests
from bs4 import BeautifulSoup
 
 
#################################
# Wikipediaを複数偉人分を同時にスクレイピング
#################################
 
import urllib.parse as parser
import urllib.request as request
from bs4 import BeautifulSoup
 
# 検索したい偉人名

 
def scrape_wikipedia():
    """リストの人物のwikipediaページからテキストデータを取得しファイルに出力する"""
    name_list = [
    "藤原道長","源頼朝", "織田信長",
    "西郷隆盛","天智天皇","平清盛","徳川家康","豊臣秀吉","坂本龍馬","伊達政宗","夏目漱石",
    "野口英世","千利休","伊藤博文","勝海舟","聖徳太子","足利義満","板垣退助","岩倉具視","伊能忠敬"
    ]
    """wikipediaページのwiki/xxxの部分に名前が入る"""
    wiki_link = "https://ja.wikipedia.org/wiki/"
    for i, name in enumerate(name_list):
        document = ""
        # 偉人の名前をurlエンコードしwikipediaのリンクに結合させて開く
        with request.urlopen(wiki_link + parser.quote(name)) as response:
            """ 例）urllib.parse.quote(str型)
            　　　# %E6%97%A5%E6%9C%AC%E8%AA """
            
            html = response.read().decode("utf-8")
            """response.read()->ページソースをbyte型オブジェクトで取得
            contents.decode("utf-8") -> byte型オブジェクトからutf-8にデコード"""
 
            # BeautifulSoup初期化
            soup = BeautifulSoup(html, "html.parser")
 
            # <p>タグ部分だけ取り出す
            p_tags = soup.find_all("p")
 
            # bs4型オブジェクトのgetText()メソッドで生の文字列だけを取り出す
            for p in p_tags:
                # p.getText()とp.textは同じ
                document += p.text
 
        with open(f"./text_file/{i}_wiki_scraping.txt", "w", encoding='utf-8') as f:
            f.write(document)
 
#################################
# 毛呂山町のHPからスクレイピング
#################################
 
def scrape_keroyamamachi():
    """該当ウェブページからスクレイピングしてファイルに出力する関数"""
    michinaga_url = "http://www.town.moroyama.saitama.jp/www/contents/1291875504380/index.html"
    yoritomo_url = "http://www.town.moroyama.saitama.jp/www/contents/1292889397071/index.html"
    nobunaga_url = "http://www.town.moroyama.saitama.jp/www/contents/1292487988201/index.html"
    saigou_url = "http://www.town.moroyama.saitama.jp/www/contents/1290560969551/index.html"
    tenji_url = "" # 該当のwebページがないため
    taira_url = "http://www.town.moroyama.saitama.jp/www/contents/1291876385940/index.html"
    tokugawa_url = "http://www.town.moroyama.saitama.jp/www/contents/1290143710337/index.html "
    toyotomi_url = "http://www.town.moroyama.saitama.jp/www/contents/1292562544108/index.html"
    sakamoto_url = "http://www.town.moroyama.saitama.jp/www/contents/1290142689032/index.html "
    date_url = "http://www.town.moroyama.saitama.jp/www/contents/1292565445039/index.html "
    natsume_url = "http://www.town.moroyama.saitama.jp/www/contents/1290559541948/index.html "
    noguchi_url = "http://www.town.moroyama.saitama.jp/www/contents/1290566269893/index.html "
    rikyu_url = "http://www.town.moroyama.saitama.jp/www/contents/1292564727547/index.html "
    ito_url = "http://www.town.moroyama.saitama.jp/www/contents/1290559412522/index.html "				
    katsu_url = "http://www.town.moroyama.saitama.jp/www/contents/1290141846297/index.html"
    syotoku_url = "http://www.town.moroyama.saitama.jp/www/contents/1288245929939/index.html"
    ashikaga_url = "http://www.town.moroyama.saitama.jp/www/contents/1292484622826/index.html"
    itagaki_url = "http://www.town.moroyama.saitama.jp/www/contents/1290564935464/index.html"
    iwakura_url = "http://www.town.moroyama.saitama.jp/www/contents/1290559645695/index.html"
    ino_url = "http://www.town.moroyama.saitama.jp/www/contents/1290143789845/index.html"


    url_list = [michinaga_url, yoritomo_url,nobunaga_url, saigou_url, tenji_url,taira_url, tokugawa_url, toyotomi_url,
    sakamoto_url, date_url, natsume_url, noguchi_url, rikyu_url, ito_url, katsu_url, syotoku_url, ashikaga_url,
    itagaki_url, iwakura_url, ino_url]
    for i, url in enumerate(url_list):
        document = ""
        if url != "":
            with request.urlopen(url) as response:
                html = response.read().decode("utf-8")
 
                # BeautifulSoup初期化
                soup = BeautifulSoup(html, "html.parser")
 
                # <p>タグ部分だけ取り出す
                p_tags = soup.find_all("body")
 
                # bs4型オブジェクトのgetText()メソッドで生の文字列だけを取り出す
                for p in p_tags:
                    # p.getText()とp.textは同じ
                    document += p.text
            with open(f"./text_file/{i}_keroyamamachi_scraping.txt", "w", encoding='utf-8') as f:
                f.write(document)
 
 
#################################
# 日本の歴史.com　からスクレイピング
#################################

def scrape_nihonnorekishi():
    """該当ウェブページからスクレイピングしてファイルに出力する関数"""
    michinaga_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%E8%97%A4%E5%8E%9F%E9%81%93%E9%95%B7/"
    yoritomo_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e6%ba%90%e9%a0%bc%e6%9c%9d/"
    nobunaga_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e7%b9%94%e7%94%b0%e4%bf%a1%e9%95%b7-2/"
    saigou_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e8%a5%bf%e9%83%b7%e9%9a%86%e7%9b%9b/"
    tenji_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e4%b8%ad%e5%a4%a7%e5%85%84%e7%9a%87%e5%ad%90/"
    taira_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e5%b9%b3%e6%b8%85%e7%9b%9b/ "
    tokugawa_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e5%be%b3%e5%b7%9d%e5%ae%b6%e5%ba%b7/ "
    toyotomi_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e8%b1%8a%e8%87%a3%e7%a7%80%e5%90%89/"
    sakamoto_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e5%9d%82%e6%9c%ac%e9%be%8d%e9%a6%ac/ "
    date_url = ""
    natsume_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e5%9d%82%e6%9c%ac%e9%be%8d%e9%a6%ac/ "
    noguchi_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%E9%87%8E%E5%8F%A3%E8%8B%B1%E4%B8%96/ "
    rikyu_url = "https://xn--u9j228h2jmngbv0k.com/2018/09/%E5%8D%83%E5%88%A9%E4%BC%91/ "
    ito_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e4%bc%8a%e8%97%a4%e5%8d%9a%e6%96%87/ "
    katsu_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%E5%8B%9D%E6%B5%B7%E8%88%9F/"			
    syotoku_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%E8%81%96%E5%BE%B3%E5%A4%AA%E5%AD%90/"
    ashikaga_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%E8%B6%B3%E5%88%A9%E7%BE%A9%E6%BA%80/"
    itagaki_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%E6%9D%BF%E5%9E%A3%E9%80%80%E5%8A%A9/"
    iwakura_url ="https://xn--u9j228h2jmngbv0k.com/2017/11/%E5%B2%A9%E5%80%89%E5%85%B7%E8%A6%96/"
    ino_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%E4%BC%8A%E8%83%BD%E5%BF%A0%E6%95%AC/"

    url_list = [michinaga_url, yoritomo_url,nobunaga_url, saigou_url, tenji_url,taira_url, tokugawa_url, toyotomi_url,
    sakamoto_url, date_url, natsume_url, noguchi_url, rikyu_url, ito_url, katsu_url, syotoku_url, ashikaga_url,
    itagaki_url, iwakura_url, ino_url]
 
    for i, url in enumerate(url_list):
        document = ""
        if url != "":
            with request.urlopen(url) as response:
                html = response.read().decode("utf-8")
 
                # BeautifulSoup初期化
                soup = BeautifulSoup(html, "html.parser")
 
                # <p>タグ部分だけ取り出す
                p_tags = soup.find_all("p")
 
                # bs4型オブジェクトのgetText()メソッドで生の文字列だけを取り出す
                for p in p_tags:
                    # p.getText()とp.textは同じ
                    document += p.text
            with open(f"./text_file/{i}_keroyamamachi_scraping.txt", "w", encoding='utf-8') as f:
                f.write(document)
 
 
#################################
# れきし上の人物.com　からスクレイピング
#################################
 
def scrape_rekishijonojinbutsu():
    """該当ウェブページからスクレイピングしてファイルに出力する関数"""
    michinaga_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%E8%97%A4%E5%8E%9F%E9%81%93%E9%95%B7/"
    yoritomo_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e6%ba%90%e9%a0%bc%e6%9c%9d/"
    nobunaga_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e7%b9%94%e7%94%b0%e4%bf%a1%e9%95%b7-2/"
    saigou_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e8%a5%bf%e9%83%b7%e9%9a%86%e7%9b%9b/"
    tenji_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e4%b8%ad%e5%a4%a7%e5%85%84%e7%9a%87%e5%ad%90/"
    taira_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e5%b9%b3%e6%b8%85%e7%9b%9b/ "
    tokugawa_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e5%be%b3%e5%b7%9d%e5%ae%b6%e5%ba%b7/ "
    toyotomi_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e8%b1%8a%e8%87%a3%e7%a7%80%e5%90%89/"
    sakamoto_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e5%9d%82%e6%9c%ac%e9%be%8d%e9%a6%ac/ "
    date_url = ""
    natsume_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e5%9d%82%e6%9c%ac%e9%be%8d%e9%a6%ac/ "
    noguchi_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%E9%87%8E%E5%8F%A3%E8%8B%B1%E4%B8%96/ "
    rikyu_url = "https://xn--u9j228h2jmngbv0k.com/2018/09/%E5%8D%83%E5%88%A9%E4%BC%91/ "
    ito_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%e4%bc%8a%e8%97%a4%e5%8d%9a%e6%96%87/ "
    katsu_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%E5%8B%9D%E6%B5%B7%E8%88%9F/"			
    syotoku_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%E8%81%96%E5%BE%B3%E5%A4%AA%E5%AD%90/"
    ashikaga_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%E8%B6%B3%E5%88%A9%E7%BE%A9%E6%BA%80/"
    itagaki_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%E6%9D%BF%E5%9E%A3%E9%80%80%E5%8A%A9/"
    iwakura_url ="https://xn--u9j228h2jmngbv0k.com/2017/11/%E5%B2%A9%E5%80%89%E5%85%B7%E8%A6%96/"
    ino_url = "https://xn--u9j228h2jmngbv0k.com/2017/11/%E4%BC%8A%E8%83%BD%E5%BF%A0%E6%95%AC/"

    url_list = [michinaga_url, yoritomo_url,nobunaga_url, saigou_url, tenji_url,taira_url, tokugawa_url, toyotomi_url,
    sakamoto_url, date_url, natsume_url, noguchi_url, rikyu_url, ito_url, katsu_url, syotoku_url, ashikaga_url,
    itagaki_url, iwakura_url, ino_url]
 
    for i, url in enumerate(url_list):
        document = ""
        if url != "":
            with request.urlopen(url) as response:
                html = response.read().decode("utf-8")
    
                # BeautifulSoup初期化
                soup = BeautifulSoup(html, "html.parser")
    
                # <p>タグ部分だけ取り出す
                p_tags = soup.find_all("p")
    
                # bs4型オブジェクトのgetText()メソッドで生の文字列だけを取り出す
                for p in p_tags:
                    # p.getText()とp.textは同じ
                    document += p.text
            with open(f"./text_file/{i}_rekishijonojinbutsu_scraping.txt", "w", encoding='utf-8') as f:
                f.write(document)
#################################
# 歴史の人物.com　からスクレイピング
#################################
def scrape_lekishnojinbutsu():
    """該当ウェブページからスクレイピングしてファイルに出力する関数"""
												
    michinaga_url = "https://r-ijin.com/fujiwarano-mitinaga/"
    yoritomo_url = "https://r-ijin.com/minamotono-yositomo/"
    nobunaga_url = "https://r-ijin.com/oda-nobunaga/"
    saigou_url = "https://r-ijin.com/saigou-takamori/"
    tenji_url = "" # 該当のwebページがないため
    taira_url = "https://r-ijin.com/tairano-kiyomori/"
    tokugawa_url = ""
    toyotomi_url = "https://r-ijin.com/toyotomi-hidenaga/"
    sakamoto_url = "https://r-ijin.com/sakamoto-ryoma/"
    date_url = "https://r-ijin.com/date-masamune/"
    natsume_url = "https://r-ijin.com/natume-souseki/"
    noguchi_url = "https://r-ijin.com/noguti-hideyo/"
    rikyu_url = "https://colorfl.net/sennorikyu-matome/"
    ito_url = "https://r-ijin.com/itou-hirobumi/"
    katsu_url = "https://r-ijin.com/katu-kaisyu/"
    syotoku_url = "https://r-ijin.com/syotokutaisi/"
    ashikaga_url = "https://r-ijin.com/asikaga-yosimitu/"
    itagaki_url ="https://r-ijin.com/itagaki-taisuke/"
    iwakura_url = "https://r-ijin.com/iwakura-tomomi/"
    ino_url = "https://r-ijin.com/inou-tadataka/"

    url_list = [michinaga_url, yoritomo_url,nobunaga_url, saigou_url, tenji_url,taira_url, tokugawa_url, toyotomi_url,
    sakamoto_url, date_url, natsume_url, noguchi_url, rikyu_url, ito_url, katsu_url, syotoku_url, ashikaga_url,
    itagaki_url, iwakura_url, ino_url]
 
    for i, url in enumerate(url_list):
        document = ""
        if url == "":
            continue
            with request.urlopen(url) as response:
                html = response.read().decode("utf-8")

                # BeautifulSoup初期化
                soup = BeautifulSoup(html, "html.parser")

                # <p>タグ部分だけ取り出す
                p_tags = soup.find_all("p")

                # bs4型オブジェクトのgetText()メソッドで生の文字列だけを取り出す
                for p in p_tags:
                    # p.getText()とp.textは同じ
                    document += p.text
            with open(f"./text_file/{i}_lekishinojinbutsu_scraping.txt", "w", encoding='utf-8') as f:
                f.write(document)
if __name__ == "__main__":
    scrape_nihonnorekishi()
    scrape_rekishijonojinbutsu()
    scrape_keroyamamachi()



#################################
# コトバンクをスクレイピング(失敗)
#################################
"""
michinaga_url = "https://kotobank.jp/word/%E8%97%A4%E5%8E%9F%E9%81%93%E9%95%B7-124699"
yoritomo_url = "https://kotobank.jp/word/%E6%BA%90%E9%A0%BC%E6%9C%9D-139240"
nobunaga_url = "https://kotobank.jp/word/%E7%B9%94%E7%94%B0%E4%BF%A1%E9%95%B7-17785"
saigou_url = "https://kotobank.jp/word/%E8%A5%BF%E9%83%B7%E9%9A%86%E7%9B%9B-67872"
tenji_url = "https://kotobank.jp/word/%E5%A4%A9%E6%99%BA%E5%A4%A9%E7%9A%87-102574"
#tenji_url2 = "https://kotobank.jp/word/%E5%A4%A9%E6%99%BA%E5%A4%A9%E7%9A%87%28%E3%81%A6%E3%82%93%E3%81%98%E3%81%A6%E3%82%93%E3%81%AE%E3%81%86%29-1566202#E6.97.A5.E6.9C.AC.E5.A4.A7.E7.99.BE.E7.A7.91.E5.85.A8.E6.9B.B8.28.E3.83.8B.E3.83.83.E3.83.9D.E3.83.8B.E3.82.AB.29"


url_list= [michinaga_url, yoritomo_url,nobunaga_url, saigou_url, tenji_url]

for i, url in enumerate(url_list):
    document = ""

    with request.urlopen(url) as response:
        html = response.read().decode("utf-8")

        # BeautifulSoup初期化
        soup = BeautifulSoup(html, "html.parser")

        # <p>タグ部分だけ取り出す
        p_tags = soup.find_all("p")

        # bs4型オブジェクトのgetText()メソッドで生の文字列だけを取り出す
        for p in p_tags:
            # p.getText()とp.textは同じ
            print(p.text)
            document += p.text
    with open(f"{i}_scraping.txt", "w", encoding='utf-8') as f:
        f.write(document)
"""




# #################################
# # 知恵の泉 (天智天皇のみ失敗)
# # ※タグは<FONT>
# #################################
# michinaga_url = "http://www7a.biglobe.ne.jp/~gakusyuu/rekisizinbutu/huziwaranomitinaga.htm"
# yoritomo_url = "http://www7a.biglobe.ne.jp/~gakusyuu/rekisizinbutu/minamotonoyoritomo.htm"
# nobunaga_url = "http://www7a.biglobe.ne.jp/~gakusyuu/rekisizinbutu/odanobunaga.htm"
# saigou_url = "http://www7a.biglobe.ne.jp/~gakusyuu/rekisizinbutu/saigoutakamori.htm"
# tenji_url = "http://www7a.biglobe.ne.jp/~gakusyuu/rekisizinbutu/nakannoooenoouzi.htm"

# url_list= [michinaga_url, yoritomo_url,nobunaga_url, saigou_url, tenji_url]

# for i, url in enumerate(url_list):
#     document = ""

#     with request.urlopen(url) as response:
#         html = response.read().decode("utf-8")

#         # BeautifulSoup初期化
#         soup = BeautifulSoup(html, "html.parser")

#         # <font>タグ部分だけ取り出す
#         font_tags = soup.find_all("FONT")

#         # bs4型オブジェクトのgetText()メソッドで生の文字列だけを取り出す
#         for font_tag in font_tags:
#             # p.getText()とp.textは同じ
#             print(font_tag.text)
#             document += font_tag.text
#     with open(f"{i}_scraping.txt", "w", encoding='utf-8') as f:
#         f.write(document)
