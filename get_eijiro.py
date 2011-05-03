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
	#maybe, eijiro rejects user-agent by python httplib. so, change user-agent value.
	h.request('GET', '/%s/UTF-8' % urllib.quote(word.encode('utf-8')), None, {'User-Agent':'Mozilla'})
	r = h.getresponse()
	data = None
	if r.status == httplib.OK:
		result = {'word':word, 'meaning':parse(r.read())}
		write_file(result['meaning'][0])
	return None

print get_meaning(u"sample")

