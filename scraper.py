#importourlibraries
import scraperwiki
import urllib2
importlxml.etree

#createavariablecalled'url'andthenreadwhat'sthere
url="http://www.staffssaferroads.co.uk/media/114997/03092012_forwebsite.pdf"
pdfdata = urllib2.urlopen(url).read()
print "The pdf file has %d bytes" % len(pdfdata)

#converttoxmlandprintsomeinfo
xmldata = scraperwiki.pdftoxml(pdfdata)
print "After converting to xml it has %d bytes" % len(xmldata)
root = lxml.etree.fromstring(xmldata)

#thislineusesxpathtofind<text>tags
lines = root.findall('.//text[@font="5"]')
print lines
for line in lines:
    print line.text

record = {} 
for line in lines:
    record["date"] = line.text
    scraperwiki.sqlite.save(['date'], record)
