# Have to import nfc read module to read card information
import nfc_read as NFC
import mysql.connector as mc


# Initialize nfc
nfc = NFC.nfc()


# test uid
uid = 0


name = ''
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


# insert query into database

def insertQ(name, uid, room):
    insertQuery = "INSERT INTO usertable (user_name, nfc_id, room) VALUE('" + \
        name+"','"+uid+"','"+room+"');"
    executeQ(connection, insertQuery)

# select query from usertable to check if uid is vaild


def selectQ(uid):
    selectQuery = "SELECT IF('"+uid+"' in (SELECT nfc_id from usertable), 'Y', 'N');"
    result = executeQ(connection, selectQuery)
    print(result[0][0])
    if result[0][0] == 'Y':
        print("Access granted.")
        name = "SELECT name FROM usertable WHERE uid = '"+uid+"';"
        status = "TRUE"
        # if this user was already granted and pass the gate
        if executeQ(connection, "SELECT pass_gate from usertable WHERE nfc_id ='"+uid+"';")[0][0]:
            # Switch the pass_gate status and notify that this user is now Exit the gate
            status = "FALSE"
            print("Good Bye.")
        updateQ(uid, status)

        return True
    else:
        print("Access denied.")
        return False

# update the usertable's pass_gate status


def updateQ(uid, status):
    try:
        updateQuery = "UPDATE usertable SET pass_gate = " + \
            status + " WHERE nfc_id ="+uid+";"
        executeQ(connection, updateQuery)
        print("Update complete.")
    except mc.Error as e:
        print(e)

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
    insertQ("Lim Jae Yong", nfc.run(), "testroom")

    while (True):
        uid = nfc.run()
        if selectQ(uid):
            print("Good Day, ", name)
        else:
            print("Please try again.")
            continue

        # Test
        # selectQ("0000")
        # Test: Not passing gate yet
        # selectQ("1111")
        # Test: Already pass the gate and ready to Exit the gate
        # selectQ("1111")
        # break
