#!/usr/bin/python3
# -*- coding: utf-8 -*-
from bottle import route, run, template, request
from subprocess import call
import os, glob, re, ntpath, yaml

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
    for (dir, _, files) in os.walk(variable_sets_path):
         for f in files:
             path = os.path.join(dir, f)
             if os.path.exists(path):
                filename = ntpath.basename(path)
                theme_name = os.path.splitext(filename)[0]
                with open(path, 'r') as f:
                    try:
                        colors = {}
                        content = yaml.load(f)

                        # If the value for a key is color (hex), then append it to the color dict
                        for key, value in content.items():
                            if(re.findall(r'#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})', str(value), re.DOTALL)):
                                colors[key] = value

                        if len(colors) > 0: 
                            output.append({ 'theme_name': theme_name, 'filename': filename, 'fullpath': path, 'colors': colors })

                    except yaml.YAMLError as exc:
                        print("Skipping. There's a yaml parsing error:", exc)

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
