# import sys
# sys.path.append('/salary')
import pytest
# importのパスでエラー吐く
# appのインポート不要説
from calcsalary_app.salary import app

@pytest.fixture()
def app():
    yield app
