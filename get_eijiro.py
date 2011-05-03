# -*- coding: utf-8 -*-

import sys
import codecs
import httplib
import urllib
import lxml.html

def write_file(target, encoding='utf-8', file_name='out.txt'):
	f = open(file_name, 'w')
	f = codecs.lookup(encoding)[-1](f)
	f.write(target)
	f.close()

def parse(html_source):
	xRoot = lxml.html.fromstring(html_source)
	meaning_path = '//div[@id="resultsList"]/ul/li[1]'
	d = xRoot.xpath(meaning_path)
	meaning_list = []
	for i in d:
		meaning_list.append(i.text_content())
	return meaning_list

def get_meaning(word):
	h = httplib.HTTPConnection("eow.alc.co.jp")
	#maybe, eijiro reject user-agent by python httplib. so, change user-agent value.
	h.request('GET', '/%s/UTF-8' % urllib.quote(word.encode('utf-8')), None, {'User-Agent':'Mozilla'})
	r = h.getresponse()
	data = None
	if r.status == httplib.OK:
		result = {'word':word, 'meaning':parse(r.read())}
		write_file(result['meaning'][0])
	return None

print get_meaning(u"sample")

"""
word = sys.argv[1]

h = httplib.HTTPConnection("eow.alc.co.jp")
#maybe, eijiro reject user-agent by python httplib. so, change user-agent value.
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
	print getMeaning("hoge")
"""