# run.py
import os
import sys
from streamlit.web import cli as stcli

if __name__ == '__main__':
    # 현재 run.py 파일이 있는 실제 폴더 경로를 알아냅니다.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 그 폴더 안에 있는 main.py의 전체 경로를 만듭니다.
    main_path = os.path.join(current_dir, "main.py")
    
    # 만약 경로에 한글이나 띄어쓰기가 있을 경우를 대비해 설정합니다.
    sys.argv = ["streamlit", "run", main_path]
    sys.exit(stcli.main())