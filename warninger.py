# Third Party Stuff
import requests

# My Stuff
from settings import Settings


def ok() -> bool:
    print("Warninger: Sending OK...")
    settings = Settings().data
    url = "http://104.248.134.56:5052/everythingisok"

    data = {"warning_id": settings["warninger"]["warning_id"]}
    headers = {"Content-type": "application/json", "Accept": "application/json"}
    print(f"POST {url} {data}")
    response = requests.post(
        url=url,
        json=data,
        headers=headers,
    )

    if response.status_code == 200:
        print(f"Success\n{response.status_code}\n{response.text}")
        return True
    else:
        print(f"Error\n{response.status_code}\n{response.text}")
        return False


if __name__ == "__main__":
    ok()
