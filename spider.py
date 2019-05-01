import urllib.request
from urllib.request import urlretrieve
import os


class Spider(object):
	"""docstring for ClassName"""
	headers = {
	"Host": "app.mi.com",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}
	def __init__(self, arg):
		super(Spider, self).__init__()
		self.url = arg
		
	#Xiao mi get the all info from sub page
	def getSubpage(self):
		response = urllib.request.urlopen(self.url)
		result = response.read().decode('UTF-8')
		#print(result)
		return result



#parser of html to get download link & basic info using Regluar Expression
def parser(html):
	pass


#save app info to Excel/CSV
def saveInfo(info):
	pass


#download application and store in disk by category
def downloadApp(url, fileName, category):
	if url is None or fileName is None or category is None:
		return False
	filePath = './apps/' + category 
	try:
		if not os.path.exists(filePath):
			os.makedirs(filePath)
			print("creat the category is ", category)
		filePath += "/" + fileName + '.apk'
		if not os.path.exists(filePath):
			print(filePath)
			urlretrieve(url, filePath)
		else:
			print("the apk exists!")
		return True
	except Exception as e:
		return False
	

#change the page number in the same category
def changePage(url, pageNumber):
	pass


#get all category in this market
def getCategory():
	pass




#change the category when the current category is done
def changeCategory(url, currentCategory, category):
	pass