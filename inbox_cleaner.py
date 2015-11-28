__author__ = 'rauts3'

import imaplib, re
global imap_conxn, auth



def _getconxn_():
    global imap_conxn
    imap_conxn = imaplib.IMAP4_SSL('imap.gmail.com', 993)

def _login_(username, passwd):
    global auth
    auth, resp = imap_conxn.login(username, passwd)
    return resp

def _getmailcount_():
    pass
def _getmailbox_():
    mailbox = []
    if auth == 'OK':
        resp, data = imap_conxn.list()
        for item in data:
            item = item.split()[-1]
            str_item = item.decode()
            mailbox.append(str_item)
    return mailbox



_getconxn_()
_login_('sameer.raut', 'noshan')
list = _getmailbox_()
print(list)














