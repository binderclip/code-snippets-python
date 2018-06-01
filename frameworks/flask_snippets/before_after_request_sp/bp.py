from flask import Blueprint

bp = Blueprint('bp', __name__)

@bp.before_request
def before_request():
    print('>>> bp before_request')


@bp.after_request
def after_request(resp):
    print('>>> bp after_request')
    print(resp)
    return resp


@bp.route('/', methods=['GET', 'POST'])
def index():
    return 'bp index'
