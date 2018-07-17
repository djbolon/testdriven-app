# services/users/project/api/users.py


from flask import Blueprint, jsonify, request, render_template

from project.api.models import User, Exrate, ListExrate
from project import db
from datetime import date

from sqlalchemy import exc


users_blueprint = Blueprint('users', __name__, template_folder='./templates')


@users_blueprint.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

@users_blueprint.route('/users', methods=['POST'])
def add_user():
    post_data = request.get_json()
    response_object = {
        'status': 'fail',
        'message': 'Invalid payload.'
    }
    if not post_data:
        return jsonify(response_object), 400
    username = post_data.get('username')
    email = post_data.get('email')
    try:
        user = User.query.filter_by(email=email).first()
        if not user:
            db.session.add(User(username=username, email=email))
            db.session.commit()
            response_object['status'] = 'success'
            response_object['message'] = f'{email} was added!'
            return jsonify(response_object), 201
        else:
            response_object['message'] = 'Sorry. That email already exists.'
            return jsonify(response_object), 400
    except exc.IntegrityError as e:
        db.session.rollback()
        return jsonify(response_object), 400


@users_blueprint.route('/users/<user_id>', methods=['GET'])
def get_single_user(user_id):
    """Get single user details"""
    response_object = {
        'status': 'fail',
        'message': 'User does not exist'
    }
    try:
        user = User.query.filter_by(id=int(user_id)).first()
        if not user:
            return jsonify(response_object), 404
        else:
            response_object = {
                'status': 'success',
                'data': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'active': user.active
                }
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404


@users_blueprint.route('/users', methods=['GET'])
def get_all_users():
    """Get all users"""
    response_object = {
        'status': 'success',
        'data': {
            'users': [user.to_json() for user in User.query.all()]
        }
    }
    return jsonify(response_object), 200

@users_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        db.session.add(User(username=username, email=email))
        db.session.commit()

    users = User.query.all()
    return render_template('index.html', users=users)








@users_blueprint.route('/exrate', methods=['GET', 'POST'])
def exrate_f():

    if request.method == 'POST':
        rate_from = request.form['rate_from']
        rate_to = request.form['rate_to']
        rate = request.form['rate']
        rate_date = request.form['rate_date']
        user = Exrate.query.filter_by(rate_date=rate_date,rate_from=rate_from,rate_to=rate_to).first()
        if not user:
        	db.session.add(Exrate(rate_from=rate_from, rate_to=rate_to, rate_date=rate_date, rate=rate))
        	db.session.commit()
        	notes='Sukses'
        else:
        	notes='Gagal'
    user =''
    
    exrates = Exrate.query.filter_by(rate_date=date.today())
    return render_template('exrate.html', exrates=exrates,user=user)

@users_blueprint.route('/addexrate', methods=['GET', 'POST'])
def add_exrate():

    if request.method == 'POST':
        rate_from = request.form['rate_from']
        rate_to = request.form['rate_to']
        today=date.today()
        user = ListExrate.query.filter_by(rate_from=rate_from,rate_to=rate_to).first()
        if not user:
        	db.session.add(ListExrate(rate_from=rate_from, rate_to=rate_to))
        	db.session.commit()
        	notes='Sukses'
        else:
        	notes='Gagal'
    user =''
    exrates = ListExrate.query.all()
    return render_template('addexrate.html', delrates=exrates,user=user)

@users_blueprint.route('/daterate', methods=['GET', 'POST'])
def daterate_f():

    if request.method == 'POST':
        rate_date = request.form['rate_date']
        exrates = Exrate.query.filter_by(rate_date=rate_date).all()
        delrates = ListExrate.query.filter_by().all()
    else:
    	exrates = Exrate.query.filter_by(rate_date=date.today()).all()
    	#exrates = db.session.query(Exrate).join(ListExrate, Exrate.rate_from == ListExrate.rate_from).first()
    	#exrates = for exrate in ListExrate.query.all()
    	delrates = ListExrate.query.all()
    	
    return render_template('ratedate.html', exrates=exrates,delrates=delrates)


@users_blueprint.route('/deleterate', methods=['GET', 'POST'])
def deleterate_f():

    if request.method == 'POST':
        rate_from = request.form['rate_from']
        rate_to = request.form['rate_to']
        ListExrate.query.filter_by(rate_from=rate_from,rate_to=rate_to).delete()
        db.session.commit()
        delrates = ListExrate.query.all()
    else:
    	delrates = ListExrate.query.all()
    	
    return render_template('deleterate.html', delrates=delrates)