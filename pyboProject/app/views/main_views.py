from flask import Blueprint


# 블루프린트 생성
bp = Blueprint('main', __name__, url_prefix='/') # 'main'은 블루프린트의 별칭

# 블루프린트에 라우팅 함수 추가
@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return 'Pybo index'