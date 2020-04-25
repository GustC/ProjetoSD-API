from app import app,db
from flask import request,abort,Response,jsonify
from app.controllers import clientController,authController,messageController

@app.route('/')
@app.route('/index')
def index():
    return "Bem vindo!"

@app.route('/singin', methods=['POST'])
def singin():
   return authController.singin()

@app.route('/singup',methods=['POST'])
def singup():
   return authController.singup() 

@app.route('/client',methods=['GET'])
def listClients():      
   return clientController.getClients()

@app.route('/client',methods=['POST'])
def saveClient():
   return clientController.saveClient()

@app.route('/email',methods=['POST'])
def sendEmails():
   return messageController.sendEmails()
@app.errorhandler(400)
def error400(error):
   print(error)
   return error
@app.errorhandler(403)
def error403(error):
   print(error)
   return "Acesso negado!" 
@app.errorhandler(404)
def error404(error):
   return error