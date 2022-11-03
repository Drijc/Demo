# import requests
# import threading
#
# data = requests.get("https://api.github.com/search/repositories?q=is:public")
# length=len(data.json()['items'])
# # print(length)
# for i in range(0,length):
#     print(data.json()['items'][i]["language"],"---->",data.json()['items'][i]['stargazers_count'], 'forks --->', data.json()['items'][i]["forks"])
#     # print(data.json()['items'][i]["forks"])
import pandas as pd
new_my_dict = [
{'a': 15, 'n': 81, 'p': 177},
{'a': 18, 'n': 24, 'p': 190},
{'a': 19, 'n': 20, 'p': 156},
{'a': 19, 'n': 20, 'p': 157776},
]
df = pd.DataFrame.from_dict(new_my_dict)
df.to_csv (r'test8.csv', index = False, header=True)