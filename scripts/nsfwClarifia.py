# Pip install the client:
# pip install clarifai


# The package will be accessible by importing clarifai:

from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

# The client takes the `API_KEY` you created in your Clarifai
# account. You can set these variables in your environment as:

# - `CLARIFAI_API_KEY`

# Then you can just instantiate a ClarifaiApp object without explicity stating the API KEY. We will look for it in your environment variable.
# app = ClarifaiApp()

app = ClarifaiApp(api_key='b7d9cb0c34b04b898f54a281ed9a68a4')


model = app.models.get('e9576d86d2004ed1a38ba0cf39ecb4b1')
image = ClImage(url='https://samples.clarifai.com/metro-north.jpg')
print model.predict([image])