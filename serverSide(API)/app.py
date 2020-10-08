from flask import Flask
from firebase import firebase

app = Flask(__name__)
URL = "https://devnation-db-thecoders.firebaseio.com/" #Link to the Database
dataBase = firebase.FirebaseApplication(URL, None)

def getCords(): #Gets all the active Cords from the DB
   result = dataBase.get('/cords',"")
   return result

@app.route('/') #Gets all the active Cords
def home():
   cords = getCords()
   cords_list=[]
   newlist=cords.values()
   for item in newlist:
      list=item.values()
      for i in list:
         cords_list.append(i)

   return str(cords_list)

@app.route('/help/<cord>') #Posts a new active cord, Example - http://127.0.0.1:5000/help/thisIsATest
def help(cord):
   response = dataBase.post('/cords',{"active":cord})
   return ""

@app.route('/delete/<cord>') #Delets an active cord ,Example - http://127.0.0.1:5000/delete/thisIsATest
def delete(cord):
   cordDict = getCords() #Get the active 
   dictToDelete = {"active" : cord}
   for key in cordDict:
      dic = cordDict[key]
      if(dictToDelete == dic):
         keyToDelete = key

   dataBase.delete('/cords',keyToDelete)
   return ""

#http://127.0.0.1:5000/delete/thisIsATest


if __name__ == "__main__":
   app.run() #Runs the web app

#meow
