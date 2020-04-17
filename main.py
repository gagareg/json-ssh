import json
import os


login = str(input("Stash login: "))
password = str(input("Stash password: "))
ssh_repo = str(input("Link to Stash with SSH"))


curl = "curl -o httpsJson.json -k -u " + login + ":" + password + ssh_repo

os.system(curl)

with open("httpsJson.json") as data_file:
    data = json.load(data_file)

text = str(data.get("ssh_key"))

with open("id_rsa_low_pub", "w") as text_file:
    text_file.write(text)

os.chmod("id_rsa_low_pub", 0o700)

os.remove("httpsJson.json")


