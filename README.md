```
            ██      ██        ██                                         
           ░██     ░░        ░██                                         
 ███     ██░██      ██ ██████░██  ██  █████  ██████  ██████      
░░██  █ ░██░██████ ░██░░░░██ ░██ ██  ██░░░██░░██░░█ ██░░░░  █████
 ░██ ███░██░██░░░██░██   ██  ░████  ░███████ ░██ ░ ░░█████ ░░░░░ 
 ░████░████░██  ░██░██  ██   ░██░██ ░██░░░░  ░██    ░░░░░██      
 ███░ ░░░██░██  ░██░██ ██████░██░░██░░██████░███    ██████       
░░░    ░░░ ░░   ░░ ░░ ░░░░░░ ░░  ░░  ░░░░░░ ░░░    ░░░░░░        
                                                 
  ██████  █████  ██████ ██    ██  █████  ██████  
 ██░░░░  ██░░░██░░██░░█░██   ░██ ██░░░██░░██░░█  
░░█████ ░███████ ░██ ░ ░░██ ░██ ░███████ ░██ ░   
 ░░░░░██░██░░░░  ░██    ░░████  ░██░░░░  ░██     
 ██████ ░░██████░███     ░░██   ░░██████░███     
░░░░░░   ░░░░░░ ░░░       ░░     ░░░░░░ ░░░      

```
### Preview your colorschemes saved in yamls on a local server and apply them.
This serves as an extension to [whizkers by metakirby5](https://github.com/metakirby5/whizkers), but could be extended to preview any ``.Xresources``-like files.

### Why
Too many nice colorschemes which I don't remember how they look like.

### Assumptions
You use ``whizkers``, you have at least *background* and *foreground*/*primary* vars defined in the color files.

### Preview
![preview](https://0x0.st/ZMz.png)
### Issues
- ~~Would've been smarter to parse the yaml with a parser, not as text~~
- ~~The scripts gets hung up over comments (the regex for finding hex colors could be more refined)~~
- The blocks of color don't exclude *background* and *foreground* (which are presented as the section background color and text)
- Supports only hex values

### Dependencies
Python3, bottle, whizkers, wz-utils
