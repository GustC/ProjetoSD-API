from flask import request,abort,Response,jsonify
from app import clients,decodeToken,user,db

def show():
    print("opa")
    return "BOA"


def getClients():
    xToken = request.headers.get('x-token')
    
    if(xToken is None):
        abort(403,description="Acesso negado")
    
    userId = decodeToken(xToken)

    us = user.query.get(userId)

    if(us is None):
        abort(403,description="Acesso negado")

    search = request.args.get("search")
    nameSearch = ""
    if( search is not None ):
        nameSearch = search
    print("Busca = ", nameSearch)

    result = clients.query.filter_by(company_id=us.company_id).all()
    print(result)    
    if not result: 
        return jsonify({"message" : "Você não possui clientes cadastros!", "data" : [] ,"status" : "success"}) 

    data = []
    for clie in result :
        data.append(clie.toMap())
    return jsonify({"data" : data ,"status" : "success"})

def saveClient():
    xToken = request.headers.get('x-token')
    if(xToken is None):
        abort(403,description="Acesso negado")

    userId = decodeToken(xToken)

    us = user.query.get(userId)

    print(us)

    email = request.form.get("email")
    name = request.form.get("name")
    if(email is None):
        abort(400, description="Preencha o campo do email!")
    if(name is None):
        abort(400, description="Preencha o campo de nome!")
    result = clients.query.filter_by(email=email).all()
    if not result:
        companyNew = clients(name = name,email = email,company_id=us.company_id)
        db.session.add(companyNew)
        db.session.commit()
        objResponse = {
            "status" : "success",
            "message" : "Cliente cadastrado com sucesso!"
        }
        return jsonify(objResponse)
    else:
        abort(400, description="Email do cliente já cadastrado")