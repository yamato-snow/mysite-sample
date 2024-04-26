import environ
# from pathlib import Path

# 環境変数を読み込む
env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# ↓ パスを変更
# path : プロジェクトパス
PROJECT_DIR = environ.Path(__file__) - 2

# path : ワークフォルダパス
BASE_DIR = environ.Path(__file__) - 3

# SECRET_KEY = '~~~'
# DEBUG = True
# ALLOWED_HOSTS = []
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# ↓ 変更
SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
DATABASES = {
    "default": env.db(),
}

# 追加もしくは変更
STATIC_ROOT = BASE_DIR("static")
STATIC_URL = "/static/"

MEDIA_ROOT = BASE_DIR("media")
MEDIA_URL = "/media/"