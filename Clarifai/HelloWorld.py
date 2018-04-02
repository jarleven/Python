from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

from os.path import expanduser
from PIL import Image


home = expanduser("~")
keyfile = home+"/.ClarifaiKey.txt"
MyKey=None
f = open(keyfile,"r")
MyKey = f.readline()
MyKey = MyKey.strip()
#print(MyKey)

app = ClarifaiApp(api_key=MyKey)

model = app.models.get('general-v1.3')

MyFile='./index.jpeg'

#response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')
response = model.predict_by_filename(MyFile)


concepts = response['outputs'][0]['data']['concepts']
for concept in concepts:
    print(concept['name'], concept['value'])
    if concept['name'] == 'fish':
        print("                     Det er ein fisk %d%%" % ((concept['value'])*100) )

Image.open(MyFile).show()

