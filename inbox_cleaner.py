__author__ = 'rauts3'
from pygmail import pygmail


def _get_unread_count():

     new_email = pygmail()
     rc = new_email.login('username', 'passwd')
     if rc == 'OK':
        count = new_email.get_mail_count()
     return count



unread_count = _get_unread_count()
print(unread_count)





