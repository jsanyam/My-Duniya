def search_to_json(search):
    from urllib2 import urlopen
    from bs4 import BeautifulSoup
    import json
    url_base='http://aninews.in/newsdetail/keyword-search/'
    search_str=search.replace(' ','-')
    url_end='.html'
    url= url_base+search_str+url_end

    html= urlopen(url)
    bsObj=BeautifulSoup(html,"html.parser")
    resultset=bsObj.findAll("div",attrs={"class":"catnewsbox"})
    list=[]
    i=0
    for result in resultset:
        i=i+1
        if(i==7):
            break
        url=result.find("a")["href"]
        html= urlopen(url)
        bsObj=BeautifulSoup(html,"html.parser")
        image=bsObj.find("meta",attrs={"property":"og:image"})["content"]
        title=bsObj.find("meta",attrs={"property":"og:title"})["content"]
        story=bsObj.find("span",attrs={"style":"text-align:left;"}).get_text()
        description=bsObj.find("meta",attrs={"name":"description"})["content"]
        # print title
        # print image
        # print description
        # print story

        list.append({"title":title,"image":image,"description":description,"story":story})
    return list
