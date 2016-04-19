from bottle import route, run, template, request
import os, glob
import re
import ntpath
from subprocess import call

command = "whizkers"
port = 9696
# TODO identify the background foreground hexs, then parsem them further to bare vars

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

def renderThemes():
    output = []
    for filepath in glob.glob(os.path.join("/home/amk/.config/whizkers/variable_sets/", '*.yaml')):
        content = open(filepath).read()
        filename = ntpath.basename(filepath)
        themename = os.path.splitext(filename)[0]
        found_hex = re.findall(r'#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})\b', content, re.DOTALL)
        found_keywords = re.findall(r'(\w+)\:', content, re.DOTALL)
        colors = {}
        for i,val in enumerate(found_hex):
            colors[found_keywords[i]] = found_hex[i]
        dict = {'themename': themename, 'filename': filename,'filepath': filepath,'keywords': found_keywords,'hex': found_hex, 'colors': colors}
        output.append(dict)

    output = sorted(output, key=lambda k: k['filename'].lower()) 
    return template('index', e=output)

@route('/')
def index():
    theme = request.query.get( "theme" )
    if theme:
        print("Received request for " + theme)
        call([command, theme])
        call(["reload-desktop"])
        return renderThemes()
    else:
        return renderThemes()

run(host='0.0.0.0', port=port, reloader=True)
