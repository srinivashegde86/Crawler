import urllib.request


def getAllLinks(url):
    html = urllib.request.urlopen(url)
    doc = str(html.read())
    start = 0
    allLinks = []
    while start != -1:
        link, start = getLink(doc, start)
        if isValid(link):
            allLinks.append(link)
    return allLinks
        
def getLink(content, start):
    hrefStart = content.find('href="', start)
    if hrefStart == -1:
        return "", -1
    
    linkStart = hrefStart + 6
    linkEnd = content.find('"', linkStart)
    return content[linkStart:linkEnd], linkEnd

def isValid(link):
    return link.find('http') != -1

def printCrawled(links):
    for link in links:
        print (link)
        
def main():
    inp = input().split()
    toBeCrawled = [inp[0]]
    crawled = []
    while len(crawled) < int(inp[1]) and len(toBeCrawled) > 0:
        url = toBeCrawled.pop(0)
        allLinks = getAllLinks(url)
        crawled.append(url)
        for link in allLinks:
            if(link not in crawled and link not in toBeCrawled):
                toBeCrawled.append(link)
        
    printCrawled(crawled)
            

if __name__ == "__main__":
    main()
