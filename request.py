import requests
from urllib.parse import urlencode

# API 요청을 위한 기본 URL 및 파라미터 설정
base_url = "https://openapi.its.go.kr:9443/trafficInfo"
params = {
    "apiKey": "ec99bd6ea9c34254b6a469b5e42a0e83",
    "type": "all",
    "routeNo": "1",
    "drcType": "all",
    "minX": "127.068227",
    "maxX": "127.069591",
    "minY": "37.293782",
    "maxY": "37.298719",
    "getType": "json"
}

encoded_params = urlencode(params)
url = f"{base_url}?{encoded_params}"

response = requests.get(url)

print("Response code:", response.status_code)
print(response.json()['body']['items'][0])

import pandas as pd

def export_json_list_to_excel(json_list, excel_file_path):
    try:
        try:
            existing_df = pd.read_excel(excel_file_path)
        except FileNotFoundError:
            existing_df = pd.DataFrame()
        new_df = pd.DataFrame(json_list)
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        combined_df.to_excel(excel_file_path, index=False)

    except Exception as e:
        print(f"An error occurred: {e}")

export_json_list_to_excel(response.json()['body']['items'], "traffic_data.xlsx")

