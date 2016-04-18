<!DOCTYPE html>
<html>
 <head>
   <meta charset="UTF-8">
   <title>whizkers-server</title>
 <style type="text/css">
 div.bcg{
 	 padding: 10px;
 }
  
 </style>
 </head>
 <body>
<ul>
  % for item in e:
  	<div class="bcg" style="background-color:{{item['colors'].get('background', "")}}">
    	<h3 style="color:{{item['colors'].get('foreground', "")}}">
    		{{item['filename']}}
    	</h3>
    	<div>
  		% for hex in item['hex']:
			<span style="color:{{hex}}">███</span>
		% end
    	</div>
    </div>
	<hr>
  % end
</ul>
 
 </body>
</html>
