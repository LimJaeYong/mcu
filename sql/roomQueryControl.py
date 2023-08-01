'''
 This is roomQueryControl source.
'''

# Have to import nfc read module to read card information
import nfc_read as NFC
import mysql.connector as mc
import time

# Initialize nfc
nfc = NFC.nfc()

# test uid
uid = 0

# connect to db



def Connect_DB():
    try:
        connectInfo = mc.connect(
            user='testAccount_mcu',
            password='0000',
            host='1.231.83.240',
            database='resident'
        )
        return connectInfo

    except mc.Error as e:
        print("Connection error: ", e)

# select query from usertable to check if uid is vaild


def selectQ(uid):
    # Check that user's pass_gate status
    if executeQ(connection, "SELECT IF('"+uid+"' in (SELECT nfc_id from usertable), 'Y', 'N');")[0][0]:
        # if TRUE
        print("pass 1, uid is registered")
        if executeQ(connection, "SELECT IF(pass_gate = TRUE, 1, 0) from usertable WHERE nfc_id = '"+uid+"';")[0][0]:
            # Check if this user granted to access this room
            print("pass 2, passed through the main gate")
            if executeQ(connection, "SELECT IF('"+roomname+"' in (SELECT room FROM usertable WHERE nfc_id = '"+uid+"'), 1, 0);")[0][0]:
                # Switch the pass_gate status and notify that this user is now Exit the gate
                print("pass 3")
                print('Access granted')
                return True
            else:
                print("Access denied.3")
        else:
            print("Access denied.2")

    else:  # if FALSE
        print("Access denied.1")
        return False


# execute the query

def executeQ(connection, query):
    try:
        cur = connection.cursor()
        cur.execute(query)
        result = cur.fetchall()
        connection.commit()
        cur.close()
        return result
    except mc.Error as e:
        print("Query execution error: ", e)


if __name__ == "__main__":
    connection = Connect_DB()
    #insertQ("Lim Jae Yong", nfc.run(), "testroom")
    roomname = 'testroom'

    while (True):
        uid = nfc.run()
        if selectQ(uid):
            print("Good Day, ", executeQ(connection, "SELECT user_name FROM usertable WHERE nfc_id ='"+uid+"';")[0][0])
            time.sleep(2)
            continue
        else:
            print("Please try again.")
            time.sleep(2)
            continue

        selectQ("0000")
        # Test: Not passing gate yet
        selectQ("1111")
        # Test: Already pass the gate and ready to Exit the gate
        # selectQ("1111")
        break
