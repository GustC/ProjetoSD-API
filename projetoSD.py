from app import app
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.run(host='0.0.0.0', port=port)