from .app import app, db
from .models import *
from flask import jsonify, request, abort

@app.route('/quiz/api/v1.0/quiz', methods=['GET'])
def get_all_questionnaires():
    return jsonify(get_all_questionnaires_db())

@app.route('/quiz/api/v1.0/quiz/<int:id>', methods=['GET'])
def get_questionnaire(id) :
    return jsonify(get_question_by_questionnaire_db(id))

@app.route('/quiz/api/v1.0/quiz', methods=['POST'])
def add_questionnaire():
    if not request.json or not 'name' in request.json :
        abort(400)
    name = request.json['name']
    return jsonify(add_questionnaire_db(name))

@app.route('/quiz/api/v1.0/quiz/<int:id>', methods=['PUT'])
def set_questionnaire(id) :
    if not request.json or not 'name' in request.json :
        abort(400)
    name = request.json['name']
    return jsonify(set_name_questionnaire(name, id))

@app.route('/quiz/api/v1.0/quiz/<int:id>', methods=['DELETE'])
def delete_questionnaire(id) :
    return jsonify(delete_questionnaire_bd(id))

@app.route('/quiz/api/v1.0/quiz/<int:id>', methods=['POST'])
def add_question(id) :
    if not request.json or not 'title' in request.json or not 'questionType' in request.json or not 'reponse' in request.json :
        abort(400)
    title = request.json['title']
    questionType = request.json['questionType']
    reponse = request.json['reponse']
    if questionType == "MultipleQuestion" :
        options = request.json['options']
        return jsonify(add_question_db(title, questionType, reponse, id, options))
    else :
        return jsonify(add_question_db(title, questionType, reponse, id))

@app.route('/quiz/api/v1.0/quiz/question/<int:id>', methods=['GET'])
def get_question(id) :
    return jsonify(get_question_db(id))

@app.route('/quiz/api/v1.0/quiz/question/<int:id>', methods=['PUT'])
def set_question(id) :
    if not request.json :
        abort(400)
    question_id = request.json['id']
    title = request.json['title']
    reponse = request.json['reponse']
    typeQuestion = request.json['questionType']
    if typeQuestion == "MultipleQuestion":
        options = request.json['options']
        return jsonify(set_question_bd(question_id, title, reponse, options))
    else :
        return jsonify(set_question_bd(question_id, title, reponse))
    
@app.route('/quiz/api/v1.0/quiz/question/<int:id>', methods=['DELETE'])
def delete_question(id) :
    return jsonify(delete_question_bd(id))
    

