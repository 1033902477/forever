import pytest
from Common.FilePath import REPORT_PATH
from Common.EMail import send_mail


if __name__ == '__main__':
    report_path = REPORT_PATH
    pytest.main(['-v', '-s', '--html=' + report_path])
    send_mail(report_path)