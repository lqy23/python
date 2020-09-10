import requests
from mysql import query


url = "http://192.144.148.91:2333/get_title_img"

res = requests.get(url)

print(res.text)

assert res.status_code == 200

assert res.json()["status"] == 200

data =res.json()["data"] 
for i in data:
    print(i.get("id"))
    sql = "select * from t_title_img where id ={}".format(i["id"])
    print(sql)
    res = query(sql)
    assert len(res) != 0
    print(res)




