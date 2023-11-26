import subprocess
import time
from datetime import datetime, time as time_object

def is_before_7_pm():
    # 현재 시간이 오후 7시 이전인지 확인
    current_time = datetime.now().time()
    return current_time < time_object(19, 0)  # 24시간 형식으로 오후 7시는 19시

print("시작: " + str(datetime.now().time()))
while is_before_7_pm():
    # request.py 스크립트 실행
    subprocess.run(["python", "request.py"])

    # 3분 (180초) 동안 대기
    time.sleep(180)

print("It's 7 PM or later. Stopping the script.")
