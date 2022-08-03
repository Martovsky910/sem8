from data import join

def create():
    style= 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '            <p{}>:{}</p>\n'.format(style, join())
    html += '            </body>\n<html>'
    with open('index.html','w') as page:
        page.write(html)
    return 