# 環境変数を参照
import os
MYAPP_USER = os.getenv('MYAPP_NAME')

print(MYAPP_USER)