from flask import (
  Flask, request, jsonify)
from settings import db, app
from models import User


@app.route('/user', methods=['GET'])
def get_all_users():

    message = {
      'status': 404,
      'message': 'Something went wrong'
    }
    try:
        data = User.query.with_entities(
          User.student_id, User.first_name,
          User.last_name, User.dob,
          User.amount_due).all()
        message.update({
          'status': 200,
          'message': 'ALl records are fetched',
          'data': data
        })
    except:
        pass
    return jsonify(message)


@app.route('/user/<int:id>', methods=['GET'])
def get_specific_user(id):

    message = {
      'status': 404,
      'message': 'User not exists'
    }
    data = User.query.with_entities(
      User.student_id, User.first_name,
      User.last_name, User.dob,
      User.amount_due).filter_by(student_id=id).all()
    if len(data) == 0:
        return jsonify(message)
    message.update({
      'status': 200,
      'message': 'ALl records are fetched',
      'data': data
    })
    return jsonify(message)


@app.route('/user', methods=['POST'])
def create_user():

    message = {
      'status': 404,
      'message': 'Something went wrong'
      }
    try:
        student_id = request.form.get('student_id', '')
        first_name = request.form.get('first_name', '')
        last_name = request.form.get('last_name', '')
        dob = request.form.get('dob', '')
        amount_due = request.form.get('amount_due', '')
        user = User(
          student_id=student_id,
          first_name=first_name,
          last_name=last_name,
          dob=dob,
          amount_due=amount_due
        )
        db.session.add(user)
        db.session.commit()
        message.update({
            'status': 201,
            'message': 'User created successfully!!! ',
            'user_id': user.student_id
        })
    except:
        pass
    resp = jsonify(message)
    return resp


@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):

    message = {
      'status': 404,
      'message': 'user not found'
    }
    try:
        new_first_name = request.form.get('first_name', None)
        new_last_name = request.form.get('last_name', None)
        new_dob = request.form.get('dob', None)
        new_amount_due = request.form.get('amount_due', None)
        try:
            current_user = User.query.get_or_404(id)
        except:
            return jsonify(message)

        if new_first_name:
            current_user.first_name = new_first_name
        if new_last_name:
            current_user.last_name = new_last_name
        if new_dob:
            current_user.dob = new_dob
        if new_amount_due:
            current_user.amount_due = new_amount_due

        db.session.commit()
        message.update({
          'status': 200,
          'message': 'User details updated successfully!!! '
        })
    except:
        pass
    resp = jsonify(message)
    return resp


@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):

    message = {
      'status': 404,
      'message': 'user not found'
    }
    try:
        current_user = User.query.get_or_404(id)
        db.session.delete(current_user)
        db.session.commit()
        message.update({
          'status': 200,
          'message': 'user record delete successfully!!! '
        })
    except:
        pass
    resp = jsonify(message)
    return resp


if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0", debug=True)



