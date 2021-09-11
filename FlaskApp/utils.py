from functools import wraps
from accounts.SqlConnection import SqlConnetion
from flask import request


def chek_apikey(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        apikey_header = request.headers['apikey']
        db = SqlConnetion()
        query = ("SELECT is_activated FROM accounts.accounts WHERE apikey=%(apikey)s")
        apikey = {'apikey': apikey_header}
        res = db.execute(query, apikey)
        for (is_activated) in res:
            if is_activated[0] == 1:
                return f(*args, **kwargs)
        return 'Unauthorized', 401
    return decorated