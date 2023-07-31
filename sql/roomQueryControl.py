'''
 This is roomQueryControl source.
It must fix for the room MCU.
'''

# Have to import nfc read module to read card information
# import nfc_read as nfc
import mysql.connector as mc


# Initialize nfc
# nfc = nfc.__init__()

# test uid
uid = 0

# connect to db
__roomname = ''


def Connect_DB():
    try:
        connectInfo = mc.connect(
            user='testAccount_mac',
            password='0000',
            host='dlawodyd.iptime.org',
            database='resident'
        )
        return connectInfo

    except mc.Error as e:
        print("Connection error: ", e)

# select query from usertable to check if uid is vaild


def selectQ(uid):
    # Check that user's pass_gate status
    if executeQ(connection, "SELECT IF(nfc_id =sss"+uid+", 1, 0) from usertable;")[0][0]:
        # if TRUE
        print("1")
        if executeQ(connection, "SELECT IF(pass_gate = TRUE, 1, 0) from usertable WHERE nfc_id = "+uid+";")[0][0]:
            # Check if this user granted to access this room
            print("2")
            if executeQ(connection, "SELECT IF('"+roomname+"' in (SELECT room FROM usertable WHERE nfc_id = "+uid+"), 1, 0);")[0][0]:
                # Switch the pass_gate status and notify that this user is now Exit the gate
                print("3")
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

    roomname = 'testroom'

    while (True):
        # uid = nfc.run()
        # selectQ(uid)

        selectQ("0000")
        # Test: Not passing gate yet
        selectQ("1111")
        # Test: Already pass the gate and ready to Exit the gate
        # selectQ("1111")
        break
