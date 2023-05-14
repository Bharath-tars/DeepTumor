import requests
from datetime import datetime
from mail import shoot_mail

docupilot_api_key = "b451c83b"
template_id = "a072630d"


def boost_report(name, email, phoneno, filename):
    data = {
        "pid": filename,
        "Pemail": email,
        "pno": phoneno,
        "pname": name,
        "predict": "88.9%",
        "result": "Detected",
        "Date": datetime.now().strftime('%Y-%m-%d')
    }

    url = f"https://api.docupilot.app/documents/create/{docupilot_api_key}/{template_id}?download=true"

    response = requests.post(url, json=data)

    response_data = response.json()
    file_url = response_data["data"]["file_url"]
    shoot_mail(file_url, name, email, phoneno, filename)
    return file_url
