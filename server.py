from bottle import route, run, template
import os, glob
import re
import ntpath

# TODO identify the background foreground hexs, then parsem them further to bare vars

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
def index():
    output = []
    for filepath in glob.glob(os.path.join("/home/amk/.config/whizkers/variable_sets/", '*.yaml')):
        content = open(filepath).read()
        filename = ntpath.basename(filepath)
        found_hex = re.findall(r'#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})\b', content, flags=re.DOTALL)
        dict = {'filename': filename,'filepath': filepath,'hex': found_hex}
        output.append(dict)
        
    output = sorted(output, key=lambda k: k['filename'].lower()) 
    return template('index', e=output)

run(host='0.0.0.0', port=9696, reloader=True)
