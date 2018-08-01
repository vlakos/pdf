import scraperwiki
import urllib2
import lxml.etree

url="http://www.acas.rs/wp-content/uploads/2017/12/Godisnji-plan-provere-za-2018.pdf"
pdfdata=urllib2.urlopen(url).read()
print "Thepdffilehas%dbytes"%len(pdfdata)
xmldata = scraperwiki.pdftoxml(pdfdata)
print "After converting to xml it has %d bytes" % len(xmldata)
print "The first 2000 characters are:", xmldata[:2000]
root = lxml.etree.fromstring(xmldata)
pages = list(root)
print "The pages are numbered:", [ page.attrib.get("number") for page in pages ]
#thisfunctionhastoworkrecursivelybecausewemighthave"<bPart1<ipart2</i</b"
def gettext_with_bi_tags(el):
    res = [ ]
    if el.text:
        res.append(el.text)
for lel in el:
    res.append("<%s" % lel.tag) 
    res.append(gettext_with_bi_tags(lel)) 
    res.append("</%s" % lel.tag)
    if el.tail:
        return "".join(res) 35
#printthefirsthundredtextelementsfromthefirstpage
page0=pages[0]
ID=0
for el in list(page0)[:100]:
    print el.tag
    if el.tag == "text":
        print el.attrib, gettext_with_bi_tags(el)
        record = {}
        record["text"] = gettext_with_bi_tags(el)
        ID = ID+1
        record["ID"] = ID
        scraperwiki.sqlite.save(["ID"],record)
        print record
