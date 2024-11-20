from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


os.makedirs("instance", exist_ok=True)

db_file = os.path.join(os.getcwd(), "instance", "example.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_file}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"

@app.route("/")
def hello_world():
    users = User.query.all()
    return render_template("index.html", users=users)

if __name__ == "__main__":
    with app.app_context():
    
        if os.path.exists(db_file):
            os.remove(db_file)
        db.create_all()

        if not User.query.first():
    
            user = User(name ="amit", email="amit122464@gmail.com")
            db.session.add(user)
            db.session.commit()

    print(f"Template path: {os.path.join(app.root_path, 'templates')}")

    app.run(host="127.0.0.1", port=5000, debug=True)




