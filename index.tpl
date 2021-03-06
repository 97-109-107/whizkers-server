<!DOCTYPE html>
<html>
 <head>
   <meta charset="UTF-8">
   <title>whizkers-server</title>
   <style type="text/css">
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
    }
    div.image-section{
        float: right;
        width: 20%;
    }
    div.bcg{
        height: 100px;
        float: left;
        width: 28%;
        padding: 10px;
        margin: 10px;
    }
    div.tinting{
        margin: 0px;
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
<script type="text/javascript">
window.onload = function () {
        function getPathFromUrl(url) {
  				return url.split("?")[0];
	  	}
	  	var oldpath, newpath;
	  	oldpath = window.location.href
		newpath = getPathFromUrl(window.location.href )
	  	if(oldpath != newpath) window.location.href = newpath
}
</script>
 </head>
 <body>
  % for item in e:
	<div class="bcg"
	style="background: {{ item.get('bg') or 'black' }}">
    <div class="tinting"
    %if item['wallpapers']:
    style="background:
    linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url('data:image/png;base64,{{item['wallpapers']}}')
    repeat center center"
    %end
    >

    	<div class="color-section">

			<h3 style="color:{{ item.get('fg') or 'white' }}">
    			{{item['theme_name']}}
    			<a class="button" style="background-color:{{ item.get('fg') or 'white' }}; color:{{ item.get('bg') or 'black' }}" href="?theme={{item['theme_name']}}">
    			Apply
    			</a>
			</h3>

  			% for key,val in item['colors'].items():
			<span style="color:{{val}}">███</span>
			% end
    	</div>

    </div>
    </div>
  % end
 
 </body>
</html>
