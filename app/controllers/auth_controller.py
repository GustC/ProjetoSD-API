from flask import request,abort,Response,jsonify,make_response
from app import user,db

def singin():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")        
        ramo = request.form.get("ramo")
        cnpjData = request.form.get("cnpj")
        if(email is None):
           abort(400, description="Preencha o campo do email!")
        if(password is None):
           abort(400, description="Preencha o campo de senha!")
        if(ramo is None):
           abort(400, description="Coloque o ramo da sua empresa!")
        if(cnpjData is None):
           abort(400, description="Coloque o cnpj da sua empresa!")
        else:
            from app import user,company     

            findCompany = company.query.filter_by(cnpj = cnpjData,).first()
            if(findCompany is not None):
               abort(400, description="O CNPJ informado já esta cadastrado!")
            findUser = user.query.filter_by(email=email).first()
            if(findUser is not None):
               abort(400, description="O email informado já esta cadastrado!")
                   
            companyNew = company(cnpj = cnpjData,ramo = ramo)
            print("company Criado")

            userNew = user(email=email,password = password,company = companyNew)
            print("user Criado")

            db.session.add(companyNew)
            db.session.commit()
            db.session.add(userNew)
            db.session.commit()

            respObject = {
                "status" : "success",
                "message" : "Usuário cadastrado com sucesso!"
            }
            return make_response(jsonify(respObject)),200
    else:
        abort(404)

def singup():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        if(email is None):
           abort(400, description="Preencha o campo do email!")
        if(password is None):
           abort(400, description="Preencha o campo de senha!")
        from app import user,company 
        userLog = user.query.filter_by(email=email,password=password).first()
        print(userLog)
        if(userLog is None):
           abort(400, description="Usuário não encontrado")

        auth_token = userLog.encode_auth_token(userLog.id)
        print(auth_token)
        return jsonify({
            "status" : "success",
            "message" : "Usuario logado!",
            "x-token" : auth_token.decode()
        })


    else:
        abort(404)