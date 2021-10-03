import mysql.connector
import os

# コネクション作成
conn = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS'),
    database=os.getenv('DB_NAME')
)

# 接続状況確認
print(conn.is_connected())

# カーソル作成
cur = conn.cursor()

# 1件取得
cur.execute("select version()")
print(cur.fetchone())

# DB操作終了
cur.close()