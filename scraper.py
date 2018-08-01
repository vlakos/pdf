#importourlibraries
import scraperwiki
import urllib2
import lxml.etree

#createavariablecalled'url'andthenreadwhat'sthere
url="http://www.acas.rs/wp-content/uploads/2017/12/Godisnji-plan-provere-za-2018.pdf"
pdfdata = urllib2.urlopen(url).read()
print "The pdf file has %d bytes" % len(pdfdata)

#converttoxmlandprintsomeinfo
xmldata = scraperwiki.pdftoxml(pdfdata)
print "After converting to xml it has %d bytes" % len(xmldata)
root = lxml.etree.fromstring(xmldata)

#thislineusesxpathtofind<text>tags
#lines = root.findall('.//text[@font="5"]')
#print lines
#for line in lines:
    #print line.text

#record = {} 
#for line in lines:
    #record["date"] = line.text
    #scraperwiki.sqlite.save(['date'], record)
