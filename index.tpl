<!DOCTYPE html>
<html>
 <head>
   <meta charset="UTF-8">
   <title>whizkers-server</title>
 <style type="text/css">
 
 body{
 	 font-family: 'monospace';
 	 background-color: #3e3e3e;
 }
 div.bcg{
 	 padding: 10px;
 }
 button{
    border: 0px none;
    border-radius: 0px;
    padding: 3px;
    margin-left: 1em;
}
  
 </style>
 </head>
 <body>
  % for item in e:
  	<div class="bcg" style="background-color:{{item['colors'].get('background', "")}}">
    	<h3 style="color:{{item['colors'].get('foreground', "")}}">
    		{{item['filename']}}
    		<button style="background-color:{{item['colors'].get('foreground', "black")}}; color:{{item['colors'].get('background', "white")}}" >Apply</apply>
    	</h3>
    	<div>
  		% for hex in item['hex']:
			<span style="color:{{hex}}">███</span>
		% end
    	</div>
    </div>
  % end
 
 </body>
</html>
