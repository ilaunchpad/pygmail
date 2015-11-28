__author__ = 'rauts3'

import imaplib, sys
global imap_conxn, auth



def _getconxn_():
    global imap_conxn
    imap_conxn = imaplib.IMAP4_SSL('imap.gmail.com', 993)

def _login_(username, passwd):
    global auth
    auth, resp = imap_conxn.login(username, passwd)

def _getmailbox_():
    mailbox = []
    if auth == 'OK':
        resp, data = imap_conxn.list()
        for item in data:
            item = item.split()[-1]
            str_item = item.decode()
            mailbox.append(str_item)
    return mailbox

def _searchmail_(tag, mailbox= None):

    if auth == 'OK':

       if mailbox is None:
            mailbox = 'Inbox'
            imap_conxn.select(mailbox)
            resp, count = imap_conxn.search(None, tag)
       else:
            imap_conxn.select(mailbox)
            resp, count = imap_conxn.search(None,tag )

       uid = count[0].decode()
       if uid:
            li_uid = uid.split()
            return li_uid

def _deletemail_(li_uid):

    for item in li_uid:
        imap_conxn.store(item,'+FLAGS', '\\Deleted')
    imap_conxn.expunge()


if __name__ == "__main__":
    _getconxn_()
    if imap_conxn:
        username = input("Enter username: ")
        passwd = input("Enter passwd: ")
        _login_(username, passwd)
        if auth == 'OK':
            mailbox = _getmailbox_()
            search_tag = input("Enter search tag :")
            format_tag = '(from '+ search_tag +')'
            li_uid = _searchmail_(format_tag)
            if li_uid:
                _deletemail_(li_uid)
                print("Task executed")
            else:
                print("Search not found")
    imap_conxn.close()
    imap_conxn.logout()
    print('Program Terminated')
    sys.exit()
























