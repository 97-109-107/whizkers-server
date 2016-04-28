<!DOCTYPE html>
<html>
 <head>
   <meta charset="UTF-8">
   <title>whizkers-server</title>
 <style type="text/css">
 *{
 	 font-family: 'monospace';
 }
 body{
 	 background-color: #3e3e3e;
   margin: 0;
   padding: 0;
 }
 img{
 	 max-height: 100px;
 }
div.color-section{
 	float: left;
 	width: 80%;
}
div.image-section{
 	float: right;
 	width: 20%;
}
 div.bcg{
 	 padding: 10px;
 	 height: 100px;
 }
 button{
    -webkit-appearance: button;
    -moz-appearance: button;
    appearance: button;
    text-decoration: none;
    color: initial;
    border: 0px none;
    border-radius: 0px;
    padding: 3px;
    margin-left: 1em;
}
a, a:link, a:visited, a:hover, a:active {
    color: inherit;
    text-decoration: none;
    font-weight: normal;
}
  
 </style>
 </head>
 <body>
  % for item in e:
    <div class="bcg"
    style="background:
    linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url('data:image/png;base64,{{item['wallpapers']}}')
    repeat center center">

    	<div class="color-section">

			<h3 style="color:{{ item['colors'].get('foreground') or item['colors'].get('primary') or 'white' }}">
    			{{item['theme_name']}}
    			<a class="button" style="background-color:{{ item['colors'].get('foreground') or item['colors'].get('primary') or 'white' }}; color:{{ item['colors'].get('background') or 'black' }}" href="?theme={{item['theme_name']}}">
    			Apply
    			</a>
			</h3>

  			% for key,val in item['colors'].items():
			<span style="color:{{val}}">███</span>
			% end
    	</div>

    </div>
  % end
 
 </body>
</html>
