# -*- codging: sjis -*-

import sys
import httplib
import lxml.html

word = sys.argv[1]

h = httplib.HTTPConnection("eow.alc.co.jp")
#maybe, eijiro filter user-agent by python httplib. so, change user-agent.
h.request("GET", "/%s/UTF-8" % word, None, {"User-Agent":"Mozilla"})
r = h.getresponse()
if r.status == httplib.OK:
	data = r.read()
	#print data
	xRoot = lxml.html.fromstring(data)
	wordclass = '//div[@id="resultsList"]//li[1]//span[@class="wordclass"]/text()'
	meaning = '//div[@id="resultsList"]//li[1]//ol/li/text()'
	#meaning = '//div[@id="resultsList"]//li[1]//ol[%s]/li[1]/text()' % str(1)
	d = xRoot.xpath(wordclass)
	print "-----" + word + "-----"
	print "".join(d)
	d = xRoot.xpath(meaning)
	print "".join(d)
