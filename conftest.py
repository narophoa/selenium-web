from selenium import webdriver
import pytest
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#class 단위 당 한번 호출
@pytest.fixture(scope='class')
def init_driver(request):
  driver = webdriver.Chrome()
  # 암시적/묵시적 대기, 최대 시간
  driver.implicitly_wait(10)
  request.cls.driver = driver
  # 브라우저 최대화
  driver.maximize_window()  
  yield
  driver.close()

def pytest_sessionstart(session):
    session.results = dict()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call':
        item.session.results[item] = result

def pytest_sessionfinish(session, exitstatus):
    print()
    print('run status code:', exitstatus)
    ret = session.results.values()

    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name('E:/selenium-web/automation-382203-d650bc10ddb4.json', scope)
    gc = gspread.authorize(credentials)
    spreadsheet = gc.open("kr_automation_test").worksheet("Checklist")
        
    #결과 값 영역 초기화
    range_to_clear = 'F2:F'
    cell_list = spreadsheet.range(range_to_clear)
    for cell in cell_list:
      cell.value = ''
    spreadsheet.update_cells(cell_list)

    #결과 입력 시작행 위치
    sheetnum = 2

    for result in ret:
        if result.passed:
            print("function name : " + str(result.nodeid))
            print("Pass!!")
            spreadsheet.update_cell(sheetnum, 6, "Pass")  # F열 6
            sheetnum = sheetnum + 1
        elif result.failed:
            print("function name : " + str(result.nodeid))
            print("Fail!!")
            spreadsheet.update_cell(sheetnum, 6, "Fail")  # F열 6
            sheetnum = sheetnum + 1
