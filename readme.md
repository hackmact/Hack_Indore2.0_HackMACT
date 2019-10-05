*Problem Statement-1 :- Waste Type Detector*

As Indore is the cleanest city in India, It is the responsibility of all citizens of Indore to maintain the cleanliness of the city.
Keeping different types of waste in different garbage boxes is a good practice but sometimes due to lack of awareness we don't know
the type of certain type of garbage. Here we are referring solid & dry as different types of garbage. We need to develop an application
which scans the garbage and determine its type also it should educate users about the type of garbage. Solution list & learning module
should be progressive in nature i.e. it should update its dictionary or knowledge about different types after every scan.

DATA SET: Collected by images of spoiled fruits images and solid waste data available on kaggle and images of food on ImageNet.
https://drive.google.com/open?id=1YExEmpczsOY04rhVtON_aKi1_jLV_8oK

OUR SOLUTION: SMARTBIN

Introduction:
It is an android app which lets the user takethe pic of some garbage and classifies it as wet or solid garbage.

Technologies Used:

ML:
1. Fastai is used to do image classification, it is a wrapper on Pytorch
2. A pretrained ResNet-32 model was used for transfer learning and training of a CNN.
3. The classifier distinguishes the images as solid and dry waste and given the processed nature of solid waste it can further classify which type of solid waste is present like solid_plastic or metal or cardboard or paper etc.
4. The images were resized to 348*512 size and they were augmented to increase the quality of dataset.

Android App:

Flask was used to create APIs to integrate ML model into the android application and to get relevant knowledge about garbage from web using 'googlesearch' API.

Solutions for Waste Management:
Scrapper1/Scrapper2 are used to get the progresive solutions for the waste management/disposal techniques for the predicted type of waste.



