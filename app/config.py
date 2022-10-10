class SystemConfig:
  DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}?charset=utf8'.format(**{
    'user': "docker",
    'password': "docker",
    'host': "db",#dbの接続先
    'port': "3306",
    'db_name': "test_database"
})

# SQLALCHEMY_DATABASE_URI = 'mysql://docker:docker@db:3306/test_database?charset=utf8'

#dialect+driver://<ユーザー名>:<パスワード>@<ホスト>:<ポート>/<データベース名>
SQLALCHEMY_TRACK_MODIFICATIONS = True

Config = SystemConfig
