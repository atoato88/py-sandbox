# -*- codging: utf-8 -*-

import httplib

h = httplib.HTTPConnection("eow.alc.co.jp")
#maybe, eijiro filter user-agent by python httplib. so, change user-agent.
h.request("GET", "/sample/UTF-8", None, {"User-Agent":"Mozilla"})
r = h.getresponse()
if r.status == httplib.OK:
	data = r.read()
	print data
print r.read()


