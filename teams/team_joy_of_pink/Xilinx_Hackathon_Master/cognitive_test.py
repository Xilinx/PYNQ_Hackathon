import requests 
import json
import os
import re
import numpy as np
url_Microsoft_Cog_Services = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize?'
Image_url = 'Anger.jpg'
#Header for Microsoft Cognitive Services requests
headers = {
    # Request headers #To confirm octet or json
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'a6a9555023d74986a23d4a6935274f88',
}

#Parameters for Microsoft Cognitive Services requests
params =  {
    # Request parameters
    #'visualFeatures':'Description'
}

#Capturing Image of the requested Item
                #os.system('raspistill -q 25 -o /home/pi/Request_Item.jpg')
				#Converting the Image into a readable binary file for passing to the Microsoft Cognitive Services
with open (Image_url, 'rb') as f:
    data2 = f.read()
				#Http Post request to the Microsoft Cognitive Services 	
response= requests.request('post',url_Microsoft_Cog_Services,json =json, data = data2, headers = headers, params = params)
data = response.json()
print(data)
				#Searching for Pattern of the required items in the image response from cognitive services

array = np.zeros(8)
array[0] = data[0]['scores']['anger']
array[1] = data[0]['scores']['contempt']
array[2] = data[0]['scores']['disgust']
array[3] = data[0]['scores']['fear']
array[4] = data[0]['scores']['happiness']
array[5] = data[0]['scores']['neutral']
array[6] = data[0]['scores']['sadness']
array[7] = data[0]['scores']['surprise']
max_value = array[0]
max_index = 0


for i in range(0,7):
    if array[i]>max_value:
        max_value = array[i]
        max_index = i

print(max_index)
     
    
     

#print(ang)
#print(cont)
#print(dis)


                #Apple_Found = re.search('apple', str(data))
                #Cabbage_Found = re.search('cabbage',str(data))
