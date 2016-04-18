<!DOCTYPE html>
<html>
 <head>
   <meta charset="UTF-8">
   <title>whizkers-server</title>
 <style type="text/css">
  
 </style>
 </head>
 <body>
<ul>
  % for item in e:
    <h3>{{item['filename']}}</h3>
  	% for hex in item['hex']:
		<span style="color:{{hex}}">███</span>
	% end
	<hr>
  % end
</ul>
 
 </body>
</html>
