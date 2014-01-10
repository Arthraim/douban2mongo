# coding= utf-8
from bs4 import BeautifulSoup
import codecs
from mongoengine import *
from movie import Movie

connect('mydouban')

import os
os.chdir("movie")
for filename in os.listdir("."):
    with codecs.open(filename, "r", "utf-8") as html_file:
        soup = BeautifulSoup(html_file.read())

        for item in soup.find_all("div", "item"):
            # <a href="http://movie.douban.com/subject/6952149/" class=""><em>绝命毒师  第五季 / Breaking Bad Season 5</em> / 超越罪恶 第五季 / 制毒师 第五季</a>
            title = item.find("li", "title").em.string.encode("utf")
            link = item.find("li", "title").a['href']
            # <li class="title">
            #     <a class="" href="http://movie.douban.com/subject/20277285/"><em>喜羊羊与灰太狼之喜气羊羊过蛇年</em> / 喜羊羊与灰太狼大电影5 / 喜羊羊与灰太狼之冒险蛇年传</a>
            # </li>
            # <li class="intro">2013-01-24(中国大陆) / 祖晴 / 梁颖 / 张琳 / 邓玉婷 / 高全胜 / 刘红韵 / 赵娜 / 中国大陆 / 简耀宗 / 86分钟 / 喜剧 / 动画 / 家庭 / 冒险 / 汉语普通话</li>
            # <li>
            #     <span class="rating3-t"></span>
            #     <span class="date">2013-01-29</span>
            #     <span class="tags">标签: 美剧 犯罪 2012</span>
            # </li>
            # <li><span class="comment">。我还会回来的！</span></li>
            li_tags = item.find_all("li")
            spans = li_tags[2].find_all("span")
            rating = spans[0]['class'][0].replace("rating","").replace("-t","")
            date = spans[1].string.encode("UTF-8").strip()
            if len(spans) > 2:
                tags = spans[2].string.encode("UTF-8").replace("标签:","").strip().split(" ")
            comment_span = item.find("span", "comment")
            if comment_span:
                comment = comment_span.string.encode("UTF-8").strip()

            print ""
            print title, link
            print rating, date, tags
            print comment

            movie = Movie()
            movie.title = title
            movie.link = link
            movie.rating = rating
            movie.date = date
            movie.tags = tags
            movie.comment = comment
            try:
                movie.save()
            except NotUniqueError as e:
                print e
                continue
