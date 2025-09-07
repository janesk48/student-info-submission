import sys
import requests 
import json 

URL = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

diction = {
    "UCID": "jsk48",
    "first_name": "Jane",
    "last_name": "Kalla",
    "github_username": "janesk48",
    "discord_username": "@janekalla7",
    "favorite_cartoon": "Tom and Jerry",
    "favorite_language": "Python",
    "movie_or_game_or_book": "Inception",
    "section": "101"
}

def post():
    exists = requests.get(URL, params={"UCID": diction["UCID"], "section": diction["section"]}, timeout= 15)
    if exists.status_code == 200:
        res = requests.put(URL, json=diction, timeout= 15)
        print("Status:", res.status_code)
        print("Body:", res.text)
    else:
        res = requests.post(URL, json=diction, timeout=15)
        print("POST:", res.status_code, res.text)

def get():
    res = requests.get(URL, params={"UCID": diction["UCID"].strip(), "section": diction["section"].strip()}, timeout=15)
    print("SENT:", res.request.method, res.request.url)
    print("GET:", res.status_code)
    print("GET:", res.text)

def put():
    res = requests.put(URL, json=diction, timeout=15)
    print("Status:", res.status_code)
    print("Body:", res.text)

def delete():
    res = requests.delete(URL, params={"UCID": diction["UCID"].strip(), "section": diction["section"].strip()}, timeout=15)
    print("Status:", res.status_code)
    print("Body:", res.text)

if __name__ == "__main__":
        
    act = sys.argv[1].lower() if len(sys.argv) > 1 else "post"
    
    try: 
        if act == "post": 
            post()
        elif act == "get": 
            get()
        elif act == "put": 
            put()
        elif act == "delete": 
            delete()
        else: print("error")
    except requests.RequestException as e:
        print("error", e)
