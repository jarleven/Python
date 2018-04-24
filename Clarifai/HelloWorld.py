"""
 pip3 install clarifai --upgrade
 pip3 install Pillow

 Most of the code is copied from :  https://github.com/Clarifai/clarifai-python

"""

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

#MyFile='./index.jpeg'
MyFile='./image3.jpg'

extension = "*.jpg"

#response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

import glob

# file-output.py
f = open('helloworld.txt','a')


for filename in glob.iglob('/home/tredea/Dropbox/Grabber-live/*.jpg'):

    checkfile = '%s' % filename
    print('%s' % checkfile)

    response = model.predict_by_filename(checkfile)



    concepts = response['outputs'][0]['data']['concepts']
    for concept in concepts:
        # print(concept['name'], concept['value'])
        if concept['name'] == 'fish':
            print("Det er ein fisk i %s sansynligheit %d%%" % (checkfile,  (concept['value'])*100) )
            f.write("\n" + "Det er ein fisk i %s sansynligheit %d%%" % (checkfile,  (concept['value'])*100) )

f.close()

#Image.open(MyFile).show()

