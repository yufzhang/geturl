import urllib2, sys

# return HTML page
def get_html(url, output_file = None):
    print "Getting page: ", url

    req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })

    r = urllib2.urlopen(req)
    charset = r.headers.getparam('charset')
    html = r.read()

    if output_file != None:
        output = open(output_file,'wb')
        output.write(html)
        output.close()

    return html, charset

def help():
    print "syntax:"
    print "    ", sys.argv[0], "url [output_file]"


if __name__ == '__main__':

    if len(sys.argv) == 2:
        html = get_html(sys.argv[1])
        print html
    elif len(sys.argv) == 3:
        html = get_html(sys.argv[1], sys.argv[2])
    else:
        help()

