#! /usr/bin/env python

import scrapy
from scrapy.crawler import CrawlerProcess
import json
import argparse
import logging
import os , sys 
import subprocess,signal

def catch_ctrl_C(sig,frame):
	print('Ctrl C \nQuit!')
	exit()


class Gid(scrapy.Spider):
	name="Gid"
	allowed_domains=["google.com"]

	#Inupt user parameters
	search_words='abc'
	size='vga'
	num='1'

	#Output 
	google_img_page_urls=list()
	list_of_img_urls=list()

	
	def set_google_img_url (self):
		#search words
		search_p_url="q="+self.search_words

		''' size = 
				 ||a     any size (default) no tbs       
		 		 ||m     medium				tbs=isz:l
				 ||l     large				tbs=isz:m
				 ||i     icon				tbs=isz:i
				 ||qsvga 400x300			tbs=isz:lt,islt:qsvga
				 || vga  640x480			tbs=isz:lt,islt:vga
				 || svga 800x600			tbs=isz:lt,islt:svga
				 || xga  1024x760			tbs=isz:lt,islt:xga
				 || 2mp  larger than 2MB	tbs=isz:lt,islt:2mp
				 || 4mp 'larger than 4MB 	tbs=isz:lt,islt:4mp
				 || you can put 6,8,10,12,15,20,40,70 MB'''
		size_normal_list=['m','l','i']
		size_larger_list=['qsvga','vga','svga','xga','2mp','4mp','6mp','8mp','10mp','12mp','15mp','20mp','40mp','70mp']
		if (self.size == 'a'):
			size_p_url=''
		elif(self.size in size_normal_list):
			size_p_url='&tbs=isz:'+self.size
		elif(self.size in size_larger_list):
			size_p_url='&tbs=isz:lt,islt:'+self.size
		else:
			print("Error in input Size")


		## Create the page urls 
		'''Number of picture you want to download: ijn= :
		  100pic        0
		  200pic 	    1
		  300pic		2
		  400pic		3
		  500pic		4
		  600pic		5
		  700pic		6
		  800pic		7'''
		loops = int(self.num)//100
		if((int(self.num)%100)>=0):
			loops+=1
		for n in range(loops):
			num_p_url='&ijn='+str(n)
			self.google_img_page_urls.append('https://www.google.com/search?tbm=isch&'+search_p_url+size_p_url+num_p_url)

	#Request Urls
	def start_requests(self):
		self.set_google_img_url()
		for url in self.google_img_page_urls:
			yield scrapy.Request(url=url,callback=self.parse)

	#Parse each url and get image urls
	def parse(self, response):
		#get the content that contain the url
		list_of_json_img=response.css('div[class="rg_meta notranslate"] ::text')
		for json_img in list_of_json_img:
			if ((len(self.list_of_img_urls))<=(int(self.num)-1)):
				url_img=json.loads(json_img.extract())["ou"]#to Extract Img url
				self.list_of_img_urls.append(url_img)

#Parse user input arguments
def args_parser():
	#Parse arguments
	parser=argparse.ArgumentParser(description='Google Images Downloader\nAuthor: Khaled Dallah',
								 formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('search_words',help="Set search words")
	parser.add_argument('-n','--num',dest='num',action='store',default='1',type=str,
						help='Number of images to download: range between [1 , 800]')
	parser.add_argument('-s','--size',dest='size',action='store',default='a',type=str,
						help="""size of images :
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
			40mp, 70mp""")
	args=parser.parse_args()
	Gid.search_words=args.search_words.replace(' ','+')
	Gid.size=args.size
	Gid.num=args.num


#Run scrapy Spider from script
def run_Gid ():
	process = CrawlerProcess({
	'USER_AGENT':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
	})
	process.crawl(Gid)
	process.start()


#Save Image links in file with name of search words
def save_links ():
	directory='download_images'
	filename=directory+'/'+Gid.search_words.replace('+','_')+'_N'+Gid.num+'_IMG_URLS.txt'
	#Create the dir
	if not os.path.exists(directory):
		os.makedirs(directory)
	#make list has each url in new line  
	img_urls_to_store=list()
	for url in Gid.list_of_img_urls:
		img_urls_to_store.append(str(url+'\n'))
	#write it to file
	with open(filename,'w+') as f:
		f.writelines(img_urls_to_store)
	return(filename)


#Download the images with Wget 
def download_images():
	#handle ctrl+c
	signal.signal(signal.SIGINT, catch_ctrl_C)

	download_answer=input('... Download images ? [Y/n] : ')
	if (download_answer=='y'):
		downloaded_img=0
		for link in Gid.list_of_img_urls:
			#down_cmd='wget -q -c --show-progress --read-timeout=10 -P "Download Images/'+Gid.search_words.replace('+','_')+'" '+link
			#out=os.system(down_cmd)
			out=subprocess.call(['wget','-q','-c', '--show-progress', '--read-timeout=10', link, '-Pdownload_images/'+Gid.search_words.replace('+','_')])
			if(out==0):
				downloaded_img+=1
				print("su")
		print("==================Result=================")
		print("... Downloaded Images : ",downloaded_img)




if __name__ == '__main__':
	#Stop Scrapy Logging
	logging.getLogger('scrapy').propagate = False

	#arguments of cmd
	args_parser()

	#Run Spider
	run_Gid()
	print("... Gid Done")

	##store in txt file
	filename=save_links()
	print("... Links save in : ",filename)

	#Download Images
	download_images()