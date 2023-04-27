import mysql.connector as mc

#연결 정보
db_config = {
    'user': 'testAccount_mac',
    'password': '0000',
    'host': 'dlawodyd.iptime.org',
    'database': 'resident'
}

conn = mc.connect(**db_config)
cur = conn.cursor()


cur.execute("INSERT INTO Test(_id, _name) VALUES(5, 'yun');")

    
conn.commit()
conn.close()