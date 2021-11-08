import requests,json,pprint,sqlite3
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def loginmc(device,username,password):
    url="https://{}:4343/v1/api/login".format(device)
    credentials = "username={}&password={}".format(username,password)
    try:
        response = requests.post(url, verify=False, data=credentials, timeout=2)
        cookie = response.json()['_global_result']['UIDARUBA']
        print("Logged into Controller")
        print("Cookie is: {}".format(cookie))
        return cookie
    except:
        print("Error Logging into Controller")
        return 401

def logoutmc(device):
    url="https://{}:4343/v1/api/logout".format(device)
    try:
        reponse = requests.post(url,timeout=2,verify=False)
        print("Logged out from Controller")
    except:
        print("Error logging out of Controller")

def getRestmc(device,cookie,url,filter):
    aoscookie = dict(SESSION = cookie)
    fullurl="https://{}:4343/v1/{}{}".format(device,url,filter)
    print("Full URL for this request if: ")
    print(fullurl)

    try:
        response=requests.get(fullurl, verify=False, cookies=aoscookie, timeout=2)
        return (response.json())
    except:
        reponse="No Data"
    return reponse

device="10.140.1.1"
username="sitita"
password="password"
vlan=""
filter=""

cookie=loginmc(device,username,password)

if cookie != "401":
    #url="configuration/object/vlan_name_id?config_path=%2Fmd&UIDARUBA={}".format(cookie)
    url="configuration/showcommand?command=show+user-table&UIDARUBA={}".format(cookie)
    print("VLAN informantion for this controller: ")
    #pprint.pprint(getRestmc(device,cookie,url,filter))
    data = getRestmc(device,cookie,url,filter)
    item_dict = data
    item = 0
    for a in item_dict['Users']:
        print(a['IP'])
        item = item+1

    print(item)
    conn = sqlite3.connect('db.sqlite3')
    print("Opened database successfully")
    cursor = conn.execute("UPDATE freespace_capacity set client='{}' where building='Centaur-Building'".format(item))
    print("UPDATE freespace_capacity set client={} where building='Centaur-Building'".format(item))
    conn.commit()
    conn.close()

    #url="configuration/object/vlan_name_id?config_path=%2Fmd&UIDARUBA={}".format(cookie)
    #url="configuration/showcommand?command=show+user-table&UIDARUBA={}".format(cookie)
    #filter="&filter=[{\"vlan_name_id.vlan-ids\" : { \"$eq\" : [\"" + vlan + "\"]}}]"
    #print("VLAN {} Information".format(vlan))
    #pprint.pprint(getRestmc(device,cookie,url,filter))

    logoutmc(device)

else:
    print("Cannot obtain information from the controller")