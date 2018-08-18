# -*- coding: utf8 -*-
from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

__author__ = 'Colorful'
__date__ = '2018/8/13 上午12:40'

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    elif isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1006
        return APIException(code=code, msg=msg, error_code=error_code)
    else:
        # TODO 添加日志
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    app.run(debug=True)
