# Google Images Scrapy Downloader
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

for help
```bash
python gid.py -h
```  
to download 
```bash
python gid.py \[-h] \[-n NUM] \[-s SIZE] search_words  
```
#### positional arguments:  
  search_words          Set search words  

#### optional arguments:  
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
                           
## Built with:
Python 3.7  
Scrapy  

## Authors:
Khaled Dallah 

## License  
[MIT](https://choosealicense.com/licenses/mit/)  
