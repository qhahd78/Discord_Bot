import requests

def cat () : 
    res = requests.get("https://api.thecatapi.com/v1/images/search")
    res_json= res.json()
    result = res_json[0]['url']
    print(res_json[0]['url'])

    return result

def dog () : 
    res = requests.get("https://api.thedogapi.com/v1/images/search")
    res_json= res.json()
    result = res_json[0]['url']
    print(res_json[0]['url'])

    return result