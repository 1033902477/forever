import pytest



"存放一些参数化的内容"
@pytest.fixture(scope='class')
def start_test():
    print('启动测试')