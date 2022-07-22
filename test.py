import requests
import dataclasses

@dataclasses
class ListEintrag:
    # Member
    url: str
    weight: int

    # Methode
    def __init__(self, jsonObject):
        self.url = jsonObject["gifLink"]
        self.weight = jsonObject["rasd"]

response = requests.get("https://bucket-v99g4h.s3.eu-central-1.amazonaws.com/data.json")
json = response.json()

# region lol
# super sexy
ourEntries = map(lambda entry:ListEintrag(entry), json["data"])

# ok sexy
def newObject(entry):
  return ListEintrag(entry)

ourEntries = map(newObject, json["data"])
# endregion
# bisschen sexy
for jsonEntry in json["data"]:
    ourEntries.append(ListEintrag(jsonEntry))

# kaum sexy
for jsonEntry in json["data"]:
    url = jsonEntry["gifLink"]
    weight = jsonEntry["rasd"]
    newEntry = ListEintrag(url, weight)
    ourEntries.append(newEntry)