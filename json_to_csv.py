import pandas as pd
import json

read_file_name = "{경로 포함 json 파일명}"
write_file_name = "{경로 포함 csv 파일명}"
with open(read_file_name, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame.from_dict(data, orient='index')

df.to_csv(write_file_name, index=False, encoding='utf-8-sig')
