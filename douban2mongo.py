# coding= utf-8
from bs4 import BeautifulSoup
import codecs

# html_file = open('book/0', 'w')
for page in range(0, 61, 15):
    with codecs.open("book/" + str(page), "r", "utf-8") as html_file:
        soup = BeautifulSoup(html_file.read())

        for item in soup.find_all("li", "subject-item"):
            # <a href="http://book.douban.com/subject/5992037/" onclick="&quot;moreurl(this,{i:'14'})&quot;" title="为他准备的谋杀">为他准备的谋杀</a>
            a_tag = item.find_all("a")[1]
            link = a_tag.get('href').encode('UTF-8')
            title = a_tag.get('title').encode('UTF-8')
            # <div class="pub">蒋峰 / 中信出版社 / 2011-4 / 29.00元</div>
            pub = item.find_all("div", "pub")[0].string.strip().encode('UTF-8')
            # <div class="short-note">
            #     <div>
            #         <span class="rating4-t"></span>
            #         <span class="date">2013-12-27 读过</span>
            #         <span class="tags">标签: 马伯庸 小说 历史 中国 祥瑞御免</span>
            #     </div>
            #     <p class="comment">blabla</p>
            # </div>
            short_note = item.find_all("div", "short-note")[0]
            spans = short_note.div.find_all("span")
            rating = spans[0]['class'][0].replace("rating","").replace("-t","")
            date = spans[1].string.encode("UTF-8").replace("读过","").strip()
            if len(spans) > 2:
                tags = spans[2].string.encode("UTF-8").replace("标签:","").strip().split(" ")
            comment = short_note.p.string.encode("UTF-8").strip()
            print title, pub, link
            print rating, date, tags
            print comment
            print ""

