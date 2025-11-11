import pandas as pd
data = {
'Name': ['Alice', 'Bob', 'Charlie'],
'Age': [24, 27, 22],
'City': ['New York', 'Los Angeles', 'Chicago']
}
df=pd.DataFrame(data)
df.to_csv('employees.csv', index=False)

df.to_json('employees.json', orient='records')


df_csv = pd.read_csv('employees.csv')
print(df_csv)


df_json = pd.read_json('employees.json')
print(df_json)


new_data = pd.DataFrame([{'Name': 'David', 'Age': 25, 'City': 'San Francisco'}])
df_csv = pd.read_csv('employees.csv')
df_csv = pd.concat([df_csv, new_data], ignore_index=True)
df_csv.to_csv('employees.csv', index=False)

pd.concat()

# new_data_json = pd.DataFrame([{'Name': 'David', 'Age': 25, 'City': 'San Francisco'}])
# df_json = pd.read_json('employees.json')
# df_json = pd.concat([df_json, new_data_json], ignore_index=True)
# df_json.to_json('employees.json', orient='records')
#
# import pandas as pd
# df_json = pd.read_json('employees.json')
# print(df_json)

# import pandas as pd
# df_csv = pd.read_csv('employees.csv')
# df_csv = df_csv[df_csv['Name'] != 'Bob']
# df_csv.to_csv('employees.csv', index=False)
#
# import pandas as pd
# df_json = pd.read_json('employees.json')
# df_json = df_json[df_json['Name'] != 'Bob']
# df_json.to_json('employees.json', orient='records')
# df_json = pd.read_json('employees.json')
# print(df_json)

