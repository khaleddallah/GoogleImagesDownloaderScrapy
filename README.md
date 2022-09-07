# Google Images Downloader using Scrapy
Python Scrapy project to download original images in full quality from Google_Images 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Scrapy.  
(Anaconda Recomended)
```bash
pip install scrapy
```
and clone the project
```bash
git clone https://github.com/khaleddallah/GoogleImageScrapyDownloader.git
```


## Usage:

download <b>NUM</b> of images about specific <b>search words</b> in specific <b>SIZE</b> 
```bash
python gid.py [-h] [-n NUM] [-s SIZE] search_words  
```    

for help 
```bash
python gid.py --help
```
<pre>
  search_words          Set search words  
  -h, --help            show this help message and exit  
  -n NUM, --num NUM     Number of images to download: range between [1 , 800]  
  -s SIZE, --size SIZE  size of images :  
                        	a      any size (default)    
                        	m      medium  
                        	l      large  
                        	i      icon  
                        	qsvga  400x300  
                        	vga    640x480  
                        	svga   800x600  
                        	xga    1024x760  
                        	2mp    larger than 2MB  
                        	4mp    larger than 4MB  
                        		or  6mp, 8mp, 10mp, 12mp, 15mp, 20mp,  
                        			40mp, 70mp   
</pre>    

for Example:
```bash
python gid.py -n 183 -s xga 'Palestine Al Quds'
```   
                           
## Built with:
Python 3.7  
Scrapy  

## Authors:
Khaled Dallah 

## License  
[MIT](https://choosealicense.com/licenses/mit/)  
