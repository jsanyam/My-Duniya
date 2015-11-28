from urllib2 import urlopen
from bs4 import BeautifulSoup


html = urlopen('http://yourstory.com/ys-stories/')
bsObj1 = BeautifulSoup(html,"html.parser")
resultset = bsObj1.findAll("a",attrs={"class":"block"})
imageset = bsObj1.findAll("div",attrs={"class":"imgWrapper block"})


# print imageset
i = 0
for result in resultset:
    try:
        image = imageset[i].findChildren()[0]["src"]

        # image
        print image

        i += 1
        html = urlopen(result['href'])
        bsObj = BeautifulSoup(html,"html.parser")
        description = bsObj.find("meta",attrs={"name":"description"})["content"]
        date = bsObj.find("meta",attrs={"property":"article:published_time"})["content"]

        #title
        print bsObj.find("h3",attrs={"class":"title color-ys"}).text.strip()

        print "\n\n"

        # whole story
        print bsObj.find("div",attrs={"class":"ys_post_content text"})

        # pub_date
        print date

        #description
        print description

        # simpletext
        print bsObj.find("div",attrs={"class":"ys_post_content text"}).get_text()

        # category
        print "yourstory"

        print("\n\n\n\n\n\n")
    except Exception as e:
        print(e)