import mysql.connector as m

def CONNECT():
    try:
        con = m.connect(host='localhost', user='root', passwd='homelander')
        cur = con.cursor()
        try:
            cur.execute('CREATE DATABASE NUTFLIXDB')
        except:
            pass
        cur.execute('USE NUTFLIXDB')
        print('CONNECTION SECURE')
        return con, cur
    except :
        print('Can\'t connect')

def Create(cur):
    try:
        cur.execute('''CREATE TABLE NUTFLIX_TABLE(
            USER_ID INTEGER PRIMARY KEY,
            USER_NAME VARCHAR(25),
            USER_PASSWORD CHAR(25),
            PAID_STATUS CHAR(3) DEFAULT 'NO',
            AMOUNT FLOAT DEFAULT 0)''')
        print('Table ready to use\n')
    except :
        print('Table ready to use\n')
con, cur = CONNECT()
Create(cur)

def SIGN_UP(con, cur):
    n = input('Enter user name:')
    p = input('Create password:')
    cur.execute('SELECT USER_ID FROM NUTFLIX_TABLE')
    x = (0,)
    while True:
        try:
            f = cur.fetchone()
            x = x + f
        except:
            break
    ID = max(x) + 1
    print('YOUR USER ID IS', ID,'                #PLEASE REMEMBER YOUR USER ID')
    cur.execute('INSERT INTO NUTFLIX_TABLE (USER_NAME, USER_PASSWORD, USER_ID) VALUES ("%s", "%s", %s)', (n, p, ID))
    con.commit()
    print('Account created successfully')
def VIEW(cur):
    n=input('Enter your USER_ID: ')
    x=input('Enter your NAME: ')
    p=input('Enter your PASSWORD: ')
    cur.execute('SELECT * FROM NUTFLIX_TABLE WHERE USER_ID= %s AND USER_NAME="%s" AND USER_PASSWORD="%s"',(n,x,p))
    X=cur.fetchone()
    if X is not None:
        print('USER_ID\tUSER_NAME\tUSER_PASS PAID\t AMOUNT')
        print('----------\t---------------\t-------------- -------\t ------------')
        for i in X:
            print(i,end='\t')
        print()
    else:
        print('ACCOUNT DOESN\'T EXISTS')
        
def VERIFY(cur):
    n=input('Enter your USER_ID: ')
    cur.execute('SELECT * FROM NUTFLIX_TABLE WHERE USER_ID= %s',(n,))
    X=cur.fetchone()
    if X is not None:
       print('YOUR ACCOUNT ALREADY EXISTS')
    else:
        print('ACCOUNT DOESN\'T EXISTS')
    
def DELETE_ACCOUNTu(cur,con):
    n=input('Enter your USER_ID:')
    x=input('Enter your NAME:')
    p=input('Enter your PASSWORD:')
    cur.execute('DELETE FROM NUTFLIX_TABLE WHERE USER_ID= %s AND USER_NAME="%s" AND USER_PASSWORD="%s"',(n,x,p))
    con.commit()
    if cur.rowcount!=0:
        print('DELETED SUCCESSFULLY')
    else:
        print('ACCOUNT DOESN\'T EXISTS')


def DELETE_ACCOUNTOO(cur,con):
    n=int(input('Enter USER_ID:'))
    cur.execute('SELECT PAID_STATUS FROM NUTFLIX_TABLE WHERE USER_ID = {}'.format(n))
    x=cur.fetchone()
    if x!=None:
        if x[0].upper()=='YES':
            print('the user has already paid can\'t delete the account')
        elif x[0].upper()=='NO':
            cur.execute('DELETE FROM NUTFLIX_TABLE WHERE USER_ID = {}'.format(n))
            con.commit()
            print('DELETED SUCCESSFULLY')
    else:
        print('ACCOUNT DOESN\'T EXIST')

def UPDATE(cur,con):
    n = int(input('Enter USER_ID:'))
    cur.execute('SELECT PAID_STATUS FROM NUTFLIX_TABLE WHERE USER_ID = {}'.format(n))
    x=cur.fetchone()
    if x is not None:
        while True:
            x = input('Amount paid or not:')
            if x.upper() == 'YES':
                p = float(input('Enter amount:'))
                cur.execute('UPDATE NUTFLIX_TABLE SET PAID_STATUS="YES", AMOUNT={} WHERE USER_ID = {}'.format(p, n))
                con.commit()
                break
            elif x.upper() == 'NO':
                cur.execute('UPDATE NUTFLIX_TABLE SET PAID_STATUS="NO", AMOUNT=0 WHERE USER_ID = {}'.format(n))
                con.commit()
                break
            else:
                print('Only input YES or NO')
    else:
        print('ACCOUNT DOESN\'T EXIST')

def DISPLAY(cur):
    cur.execute('SELECT USER_ID,PAID_STATUS,AMOUNT FROM NUTFLIX_TABLE')
    print('USER_ID\tPAID\tAMOUNT')
    for i in cur:
        for j in i:
            print(j,end='\t')
        print()




print('|------------|')
print('|NUTFLIX|')
print('|------------|')
print()
print('ENTER')
print('---------')
print('\t1 If you are a customer')
print('\t2 If you are an operator')
x=input(':')
if x=='1':
    while True:
        print()
        print('ENTER')
        print('---------')
        print('\t 1 for SIGN UP')
        print('\t 2 to CHECK ACCOUNT')
        print('\t 3 to VIEW ALL INFO')
        print('\t 4 for DELETE ACCOUNT')
        print('\t 0 to EXIT')
        n=input(':')
        if n=='1':
            SIGN_UP(con, cur)
        elif n=='2':
            VERIFY(cur)
        elif n=='3':
            VIEW(cur)
        elif n=='4':
            DELETE_ACCOUNTu(cur,con)      
        elif n=='0':
            con.close()
            print('thank for using NUTFLIX')
            break
        else:
            print('\nENTER CORRET OPTIONS\n')
elif x=='2':
    while True:
        print()
        print('ENTER')
        print('\t 1 to UPDATE')
        print('\t 2 to DISPLAY ACCOUNTS')
        print('\t 3 to DELETE ACCOUNT')
        print('\t 0 to EXIT')
        n=input(':')
        if n=='1':
            UPDATE(cur,con)
        elif n=='2':
            DISPLAY(cur)
        elif n=='3':
            DELETE_ACCOUNTOO(cur,con)
        elif n=='0':
            con.close()
            print('thank for using NUTFLIX')
            break
        else:
            print('\nENTER CORRET OPTIONS\n')
else:
    print('\nENTER CORRET OPTIONS\n')