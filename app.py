from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)

# ইউজার মডেল তৈরি
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)

# হোমপেজ ও ফর্ম লোড
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')

        if name and phone:
            new_user = User(name=name, phone=phone)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))  # Redirect to prevent re-submission

    users = User.query.all()
    users_data = [{"id": user.id, "name": user.name, "phone": user.phone} for user in users]
    return render_template('index.html', users=users_data)


@app.route('/winner', methods=['POST'])
def save_winner():
    data = request.json
    winner_name = data.get('name')
    winner_phone = data.get('phone')

    if winner_name and winner_phone:
        new_winner = Winner(name=winner_name, phone=winner_phone)
        db.session.add(new_winner)
        db.session.commit()
        return jsonify({"message": "Winner saved successfully!"}), 200
    return jsonify({"message": "Invalid data"}), 400

@app.route('/winners')
def winners_list():
    winners = Winner.query.order_by(Winner.timestamp.desc()).all()
    return render_template('winners.html', winners=winners)




# বিজয়ী সংরক্ষণের জন্য নতুন মডেল
class Winner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

# নতুন টেবিল তৈরি
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
