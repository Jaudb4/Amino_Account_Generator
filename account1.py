import random,string,hashlib,base64,importlib,threading
import os

try:
    import amino

except:
    print("Error Faild To Import 'Amino' Library ")
    print("Check Your Internet Connection")
    print("Please Restart The Tool ")
    print("")
    os.system("exit")


def deviceid_generator():
    return str('01' + (hardwareInfo := hashlib.sha1(''.join(random.choices(string.ascii_uppercase + string.digits, k = 1000)).encode("utf-8"))).hexdigest() + hashlib.sha1(bytes.fromhex('01') + hardwareInfo.digest() + base64.b64decode("6a8tf0Meh6T4x7b0XvwEt+Xw6k8=")).hexdigest()).upper()
device=deviceid_generator()

def account_generator():

    client = amino.Client()

    email = input("Enter The Account Email: ")
    if(email == "!Back"):
        account_generator()

    print("")

    client.request_verify_code(email=email)
    verify = input("Enter The Verification Code: ")
    client.register(nickname="test", email=email, password="123456789h", deviceId=device)
    client.verify(email=email,code=verify)
    print("")
    print("Account Created Sucsesfulyy")
    print("")


    i = input("Create Another Account? (Y/N): ")
    if(i == "Y"):
        account_generator()

account_generator()
