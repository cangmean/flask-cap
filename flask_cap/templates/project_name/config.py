"""
项目配置文件
"""
import os

ROOT_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
DOWN_DIR = os.path.join(
    ROOT_DIR,
    'downloads',
)

DEBUG = True
SECRET_KEY = b'flask_cap make a project'
DB_CONFIG = dict(
    host='127.0.0.1',
    db='{{ project_name }}',
    username='root',
    password='654321',
)

try:
    from local_seetings import LOCAL_DB_CONFIG
    DB_CONFIG.update(LOCAL_DB_CONFIG)
    print('db config: ', DB_CONFIG)
except ImportError:
    pass

# 数据库连接
DB_URI = "mysql+pymysql://{}:{}@{}/{}?charset=utf8".format(
    DB_CONFIG['username'], DB_CONFIG['password'],
    DB_CONFIG['host'], DB_CONFIG['db'],
)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

# alioss 配置
internal_url = ''
external_url = ''
ACCESS_ID = ''
ACCESS_SECRET = ''
BUCKET_NAME = ''