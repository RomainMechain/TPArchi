from .app import app, db
from .models import Questionnaire, Question, SimpleQuestion, MultipleQuestion
from sqlalchemy.orm import sessionmaker

@app.cli.command('init_database')
def init_database():
    db.create_all()
    Session = sessionmaker(bind=db.engine)
    session = Session()
    q1 = Questionnaire('Questionnaire 1')
    session.add(q1)
    q2 = Questionnaire('Questionnaire 2')
    session.add(q2)
    q3 = Questionnaire('Questionnaire 3')
    session.add(q3)
    quest1 = SimpleQuestion('Question numéro 1', 1, 'Réponse 1')
    session.add(quest1)
    quest2 = MultipleQuestion('Question numéro 2', 2, 'Option1,Option2,Option3', 1)
    session.add(quest2)
    quest3 = SimpleQuestion('Question numéro 3', 2, 'Réponse 3')
    session.add(quest3)
    session.commit()
    session.close()
    