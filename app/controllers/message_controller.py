from flask import request,abort,Response,jsonify
from app import clients,message,decodeToken,user,db,config,message_clients
import json


def sendEmails():
    xToken = request.headers.get('x-token')
    if(xToken is None):
        abort(403,description="Acesso negado")

    userId = decodeToken(xToken)

    us = user.query.get(userId)
    if(us is None):
        abort(403,description="Acesso negado")
    if(request.form.get("users[]") is None):
        abort(400, description="Selecione os destinatários")
    users = request.form.getlist("users[]")
    messageData = request.form.get("message")
    if(users is None or len(users[0])==0):
        abort(400, description="Selecione os destinatários")
    if(messageData is None):
        abort(400, description="Preencha o campo de messagem")
    
    newMessage = message.Message(message = messageData,user_id=us.id)
    db.session.add(newMessage)
    db.session.commit()
    data = []
    for userData in users:   
        newMessegeClient = message_clients.Message_Client(message_id=newMessage.id,client_id=json.loads(userData)["id"])
        db.session.add(newMessegeClient)
        db.session.commit()
        data.append(json.loads(userData))
    
    producer(data)

    objResponse = {
        "status" : "success",
        "message" : "Emails enviados com sucesso!"
    }
    return jsonify(objResponse)

def producer(jsonData):
    import json
    from kafka import KafkaProducer
    producer = KafkaProducer(bootstrap_servers=config.Config.KAFKA_SERVER,
                            value_serializer=lambda v: json.dumps(v).encode('utf-8'))    
    future = producer.send(config.Config.TOPIC_NAME, value=jsonData)
    result = future.get(timeout=60)