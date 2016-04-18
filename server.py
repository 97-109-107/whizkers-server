from bottle import route, run, template
import os, glob
import re

# TODO identify the background foreground hexs, then parsem them further to bare vars

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
def index():
    output = ""
    for filename in glob.glob(os.path.join("/home/amk/.config/whizkers/variable_sets/", '*.yaml')):
        content = open(filename).read()
        output += "<h3>"+filename+"</h3>"
        inside_brackets = re.findall(r'#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})\b', content, flags=re.DOTALL)
        output += "<div><b>"
        for attributes in inside_brackets:
            output += "<span style='color:"+attributes+"'>"+attributes+"</span><br>"
        output += "</b></div>"
    return output

run(host='0.0.0.0', port=9696, reloader=True)
