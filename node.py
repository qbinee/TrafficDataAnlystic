import os
import pandas as pd
from simpledbf import Dbf5

def read_dbf(file_path):
    """ .dbf 파일을 읽어서 pandas 데이터프레임으로 반환하는 함수 """
    dbf = Dbf5(file_path, codec='cp949')
    return dbf.to_dataframe()

def merge_same_name_dbf_files(root_dirs, file_names):
    """ 동일한 이름의 .dbf 파일들을 여러 디렉토리에서 찾아서 합치는 함수 """
    merged_data = {}

    for file_name in file_names:
        all_dataframes = []

        for root_dir in root_dirs:
            file_path = os.path.join(root_dir, file_name)
            if os.path.exists(file_path):
                df = read_dbf(file_path)
                all_dataframes.append(df)

        merged_data[file_name] = pd.concat(all_dataframes, ignore_index=True)

    return merged_data

root_directories = ['[2022-12-12]NODELINKDATA', '[2022-12-28]NODELINKDATA', '[2023-02-10]NODELINKDATA', '[2023-03-29]NODELINKDATA', '[2023-05-19]NODELINKDATA', '[2023-06-19]NODELINKDATA', '[2023-07-17]NODELINKDATA', '[2023-08-18]NODELINKDATA', '[2023-08-29]NODELINKDATA', '[2023-09-22]NODELINKDATA', '[2023-10-13]NODELINKDATA', '[2023-11-13]NODELINKDATA']  # 연도별 폴더 리스트
file_names = ['MOCT_LINK.dbf', 'MOCT_NODE.dbf', 'MULTILINK.dbf', 'TURNINFO.dbf']  # 합치고자 하는 파일 이름들
file_names = ['MULTILINK.dbf']

merged_data = merge_same_name_dbf_files(root_directories, file_names)
keyword = '광교'

excel_file = 'merge_data.xlsx'
# 통합된 데이터프레임 확인
for file_name, df in merged_data.items():
    print(f"--- {file_name} ---")
    print(df)
    # if file_name == 'MOCT_NODE.dbf':
    #     print(df[df['NODE_NAME'].str.contains(keyword, na=False)])
    #     df[df['NODE_NAME'].str.contains(keyword, na=False)].to_excel(excel_file, index=False) # 찾은 노드 정보를 excel에 저

    if file_name == 'MULTILINK.dbf':
        print(df.to_excel("link_road_no.xlsx", index=False))





