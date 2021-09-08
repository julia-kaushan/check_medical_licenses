import uuid


from accounts.SqlConnection import SqlConnetion
from accounts.account import Account

class AccountRepository:
    def __init__(self):
        self.db = SqlConnetion()

    def register(self, email: str):
        account = Account()
        account.email = email
        account.apikey = str(uuid.uuid4())
        add_account = ("INSERT INTO accounts.accounts "
                       "(email, apikey) "
                       "VALUES (%(email)s, (%(apikey)s))")
        date_account = {'email': account.email, 'apikey': account.apikey}
        self.db.execute(add_account, date_account)
        return account