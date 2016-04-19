#!/usr/bin/python3
from bottle import route, run, template, request
import os, glob, re, ntpath
from subprocess import call

#             ██      ██        ██                                         
#            ░██     ░░        ░██                                         
#  ███     ██░██      ██ ██████░██  ██  █████  ██████  ██████      
# ░░██  █ ░██░██████ ░██░░░░██ ░██ ██  ██░░░██░░██░░█ ██░░░░  █████
#  ░██ ███░██░██░░░██░██   ██  ░████  ░███████ ░██ ░ ░░█████ ░░░░░ 
#  ░████░████░██  ░██░██  ██   ░██░██ ░██░░░░  ░██    ░░░░░██      
#  ███░ ░░░██░██  ░██░██ ██████░██░░██░░██████░███    ██████       
# ░░░    ░░░ ░░   ░░ ░░ ░░░░░░ ░░  ░░  ░░░░░░ ░░░    ░░░░░░        
#                                                  
#   ██████  █████  ██████ ██    ██  █████  ██████  
#  ██░░░░  ██░░░██░░██░░█░██   ░██ ██░░░██░░██░░█  
# ░░█████ ░███████ ░██ ░ ░░██ ░██ ░███████ ░██ ░   
#  ░░░░░██░██░░░░  ░██    ░░████  ░██░░░░  ░██     
#  ██████ ░░██████░███     ░░██   ░░██████░███     
# ░░░░░░   ░░░░░░ ░░░       ░░     ░░░░░░ ░░░      
#
# https://github.com/97-109-107/whizkers-server
# Depends on whizkers (https://github.com/metakirby5/whizkers) by metakirby5

# The command in your PATH to load the them, will be executed with the theme name as the last element
command_load = os.getenv('WHIZ_EXE_CMD', "whizkers")
# The command in your PATH to restart the programs/wm (by default fullsalvo's wz-utils)
command_reload = os.getenv('WHIZ_EXE_CMD', "reload-desktop")
# Port for the server
port = os.getenv('WHIZ_SERV_PORT', 9696)
# location of your yaml variable sets
variable_sets_path = os.getenv('WHIZ_SERV_VPATH',os.path.join(os.path.expanduser("~"), ".config/whizkers/variable_sets/"))

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

def renderThemes():
    output = []
    for filepath in glob.glob(os.path.join(variable_sets_path, '*.yaml')):
        content = open(filepath).read()
        filename = ntpath.basename(filepath)
        themename = os.path.splitext(filename)[0]
        #FIXME what about colors defined by words (ex. 'cyan')
        found_hex = re.findall(r'#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})\b', content, re.DOTALL)
        #the '\s' is used to only pick up only actual values, and not nesting in yaml
        found_keywords = re.findall(r'(\w+)\:\s', content, re.DOTALL)
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
        call([command_load, theme])
        call([command_reload])
        return renderThemes()
    else:
        return renderThemes()

run(host='0.0.0.0', port=port, reloader=True)
