import urllib.request


sample_url = 'https://AlanSimpson.me/python/sample.html'
thepage = urllib.request.urlopen(sample_url)
status = thepage.code
print(type(thepage))