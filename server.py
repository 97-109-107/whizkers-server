#!/usr/bin/python3
# -*- coding: utf-8 -*-
import io, os, glob, re, ntpath, yaml
import base64
from bottle import route, run, template, request
from subprocess import call
from PIL import Image, ImageOps

#			 ██	  ██		██										 
#			░██	 ░░		░██										 
#  ███	 ██░██	  ██ ██████░██  ██  █████  ██████  ██████	  
# ░░██  █ ░██░██████ ░██░░░░██ ░██ ██  ██░░░██░░██░░█ ██░░░░  █████
#  ░██ ███░██░██░░░██░██   ██  ░████  ░███████ ░██ ░ ░░█████ ░░░░░ 
#  ░████░████░██  ░██░██  ██   ░██░██ ░██░░░░  ░██	░░░░░██	  
#  ███░ ░░░██░██  ░██░██ ██████░██░░██░░██████░███	██████	   
# ░░░	░░░ ░░   ░░ ░░ ░░░░░░ ░░  ░░  ░░░░░░ ░░░	░░░░░░		
#												  
#   ██████  █████  ██████ ██	██  █████  ██████  
#  ██░░░░  ██░░░██░░██░░█░██   ░██ ██░░░██░░██░░█  
# ░░█████ ░███████ ░██ ░ ░░██ ░██ ░███████ ░██ ░   
#  ░░░░░██░██░░░░  ░██	░░████  ░██░░░░  ░██	 
#  ██████ ░░██████░███	 ░░██   ░░██████░███	 
# ░░░░░░   ░░░░░░ ░░░	   ░░	 ░░░░░░ ░░░	  
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
variable_sets_path = os.getenv('WHIZ_SERV_VPATH',os.path.expanduser("~/.config/whizkers/variable_sets"))

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
						content = yaml.load(f)
						colors, wallpapers = parse(content)
						if wallpapers or colors:
							output.append({ 'theme_name': theme_name, 'filename': filename, 'fullpath': path, 'colors': colors, 'wallpapers': make_thumb(wallpapers) })

					except yaml.YAMLError as exc:
						print("Skipping. There's a yaml parsing error:", exc)

	output = sorted(output, key=lambda k: k['filename'].lower()) 
	return (template('index', e=output), output)

def parse(d, path=[], colors=None, wallpapers=None):
	colors = colors or {}
	wallpapers = wallpapers or ""
	for k,v in d.items():
		if isinstance(v, (int, float, list, type(None))):
			pass
		elif isinstance(v, str):
			path.append(k)
			if looks_like_color(v):
				colors[".".join(path)] = v
			elif looks_like_wallpaper(v):
				wallpapers = os.path.expanduser(v)
			path.pop()
		elif isinstance(v, dict):
			path.append(k)
			colors, wallpapers = parse(v, path, colors, wallpapers)
			path.pop()
		else:
			print("###Type {} not recognized: {}.{}={}".format(type(v), ".".join(path),k, v))
	return colors, wallpapers 

def looks_like_wallpaper(s):
	if re.findall(r'\.(jpe?g|png|gif|bmp)', s, re.IGNORECASE or re.DOTALL):
		return True
	return False

def looks_like_color(s):
	if re.findall(r'#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})', s, re.DOTALL):
		return True
	return False

def make_thumb(wallpapers):
	if len(wallpapers) > 0:
		with open(wallpapers, "rb") as imageFile:
			str = base64.b64encode(imageFile.read())
			return str

@route('/')
def index():
	theme = request.query.get( "theme" )
	template, output = renderThemes()
	if theme:
		#filter through the whole list of themes for the one just requested, get the full path
		theme_path = list(filter(lambda i: i['theme_name'] == theme, output))[0]['fullpath']
		print("located ")
		call([command_load, theme_path])
		call([command_reload])
	return template

run(host='0.0.0.0', port=port, reloader=True)
