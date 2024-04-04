from .app import app, db  
from sqlalchemy.orm import sessionmaker
from flask import url_for

class Questionnaire (db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String (100))
    
    def __init__ (self , name):
        self.name = name
        
    def __repr__ (self):
        return "<Questionnaire (%d) %s>" % (self.id , self.name)
    
    def to_json (self):
        json ={
            'url' : 'http://127.0.0.1:5000'+url_for('get_questionnaire' , id = self.id),
            'id': self.id ,
            'name':self.name ,
        }
        return json
    
class Question (db.Model):
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String (120))
    questionType = db.Column(db.String (120))
    questionnaire_id = db.Column(db.Integer , db. ForeignKey ('questionnaire.id'))
    questionnaire = db. relationship ("Questionnaire", backref = db. backref ("questions", lazy="dynamic"))
    __mapper_args__ = {
        'polymorphic_identity':'question',
        'with_polymorphic':'*',
        'polymorphic_on':questionType
    }
    
    def __init__(self, title, questionType, questionnaire_id) :
        self.title = title
        self.questionType = questionType
        self.questionnaire_id = questionnaire_id
        
    def to_json (self) :
        json = {
            'url' : 'http://127.0.0.1:5000'+url_for('get_question', id = self.id),
            'id' : self.id,
            'title' : self.title,
            'questionType' : self.questionType,
            'questionnaire_id' : self.questionnaire_id
        }
        return json
        
class SimpleQuestion(Question) : 
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key = True)
    reponse = db.Column(db.String(120))
    __mapper_args__ = {
        'polymorphic_identity' : 'SimpleQuestion',
        'with_polymorphic':'*',
        'polymorphic_load': 'inline'
    }
    
    def __init__(self, title, questionnaire_id, reponse):
        super().__init__(title, "SimpleQuestion", questionnaire_id)
        self.reponse = reponse
    
    def __repr__(self):
        return "<SimpleQuestion (%d) %s>" % (self.id, self.title)
    
    def to_json(self):
        json = super().to_json()
        json['reponse'] = self.reponse
        return json
    
class MultipleQuestion(Question):
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    options = db.Column(db.String(120))
    reponse = db.Column(db.Integer)
   
    __mapper_args__ = {'polymorphic_identity': 'MultipleQuestion', 'with_polymorphic': '*', 'polymorphic_load': 'inline'}
    def __init__(self, title, questionnaire_id, options, reponse):
        super().__init__(title, "MultipleQuestion", questionnaire_id)
        self.options = options
        self.reponse = reponse
 
    def __repr__(self):
        return "<MultipleQuestion (%d) %s>" % (self.id, self.title)
    
    def to_json(self):
        json = super().to_json()
        json['options'] = self.options
        json['reponse'] = self.reponse
        return json
    
def get_all_questionnaires_db ():
    Session = sessionmaker(bind=db.engine)
    session = Session()
    res = session.query(Questionnaire).all()
    session.close()
    res_json = []
    for r in res:
        res_json.append(r.to_json())
    return res_json

def get_questionnaire_db(id):
    Session = sessionmaker(bind=db.engine)
    session = Session()
    res = session.query(Questionnaire).filter(Questionnaire.id == id).first()
    session.close()
    res_json = res.to_json()
    return res_json

def get_question_by_questionnaire_db(id):
    Session = sessionmaker(bind=db.engine)
    session = Session()
    res = session.query(Question).filter(Question.questionnaire_id == id).all()
    session.close()
    lst = []
    for r in res:
        lst.append(r.to_json()['url'])
    return lst
    
def get_question_db(id):
    Session = sessionmaker(bind=db.engine)
    session = Session()
    res = session.query(Question).filter(Question.id == id).first()
    session.close()
    res_json = res.to_json()
    return res_json
    
def add_questionnaire_db(name):
    Session = sessionmaker(bind=db.engine)
    session = Session()
    q1 = Questionnaire(name)
    session.add(q1)
    session.commit()
    session.close()
    
def add_question_db(title, questionType, reponse, questionnaire_id, option=False):
    Session = sessionmaker(bind=db.engine)
    session = Session()
    if questionType == "SimpleQuestion":
        q1 = SimpleQuestion(title, questionnaire_id, reponse)
    else:
        q1 = MultipleQuestion(title, questionnaire_id, option, reponse)
    session.add(q1)
    session.commit()
    session.close()
    id_json = get_last_question_id()
    return id_json
    
def set_name_questionnaire(name, questionnaire_id):
    Session = sessionmaker(bind=db.engine)
    session = Session()
    res = session.query(Questionnaire).filter(Questionnaire.id == questionnaire_id).first()
    res.name = name
    session.commit()
    session.close()
    
def delete_questionnaire_bd(questionnaire_id):
    Session = sessionmaker(bind=db.engine)
    session = Session()
    questions = session.query(Question).filter(Question.questionnaire_id == questionnaire_id).all()
    for question in questions:
        session.delete(question)
    res = session.query(Questionnaire).filter(Questionnaire.id == questionnaire_id).first()
    session.delete(res)
    session.commit()
    session.close()

def set_question_bd(question_id, title, reponse, option=False) :
    Session = sessionmaker(bind=db.engine)
    session = Session()
    question = session.query(Question).filter(Question.id == question_id).first()
    question.title = title
    question.reponse = reponse
    if option != False:
        question.options = option
    session.commit()
    session.close()

def delete_question_bd(question_id) :
    Session = sessionmaker(bind=db.engine)
    session = Session()
    question = session.query(Question).filter(Question.id == question_id).first()
    session.delete(question)
    session.commit()
    session.close()

def get_last_question_id() :
    Session = sessionmaker(bind=db.engine)
    session = Session()
    res = session.query(Question).order_by(Question.id.desc()).first()
    session.close()
    return res.to_json()

    
