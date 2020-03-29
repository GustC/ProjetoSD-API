from app import app,db
from flask import request,abort,Response,jsonify
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/singin', methods=['POST'])
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
            userNew = user(email=email,password = password)
            companyNew = company(cnpj = cnpjData,ramo = ramo,user=userNew)
            db.session.add(userNew)
            db.session.commit()
            db.session.add(companyNew)
            db.session.commit()
            return "Usuário cadastrado com sucesso!"
    else:
        abort(404)

@app.route('/singup',methods=['POST'])
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
        return jsonify({
           "message" : "Usuario logado!",
           "data" : userLog
        })


    else:
        abort(404)

@app.errorhandler(400)
def error400(error):
    print(error)
    return error
@app.errorhandler(404)
def error404(error):
    return error