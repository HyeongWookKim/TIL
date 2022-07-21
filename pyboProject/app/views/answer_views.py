from datetime import datetime

from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from app import db
from app.models import Question, Answer


bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>', methods=('POST',))
def create(question_id):
    question = Question.query.get_or_404(question_id)
    content = request.form['content']
    answer = Answer(content=content, create_date=datetime.now())
    question.answer_set.append(answer)
    # 위에 적힌 answer_set() 함수를 사용하지 않고, 아래와 같이 코드를 작성할 수도 있음
    # answer = Answer(question=question, content=content, create_date=datetime.now())
    # db.session.add(answer)
    db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))