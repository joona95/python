
# 파이썬에서 mysql 연동하기
# pymysql 라이브러리 사용하여 CRUD 간단표현

import pymysql

# 데이터베이스 연결 (주소, 사용자, 비번, db명, 캐릭터셋, ...)
# MySQL Connection 연결

conn = pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8', )

 

curs = conn.cursor(pymysql.cursors.DictCursor)

 

# ==== select example ====

sql = "select * from customer"

curs.execute(sql)

 

# 데이타 Fetch

rows = curs.fetchall()

print(rows)

 

# ==== insert example ====

sql = """insert into customer(name,category,region)

         values (%s, %s, %s)"""

curs.execute(sql, ('홍길수', 1, '서울'))

curs.execute(sql, ('조연우', 2, '서울'))


 

# ==== update OR delete example ====

sql = """update customer

         set region = '서울'

         where region = '서울특별시'"""

curs.execute(sql)



