import hashlib
info = """
  Name            : TEXT2HASH
  Created By      : Niklas Tageby
  Blog            : bullplay.org
  Documentation   : https://github.com/MrLaserSuit
  License         : FREE
  Thanks to       : Python community
"""
# We are going to build a text2hash encoder and using 6 different hashes


#We create six different function and connect them to our if statement below --_--
def md5hash():
    user = str(input("Enter the text to Hash(MD5 Hash):"))
    print("String ----->", user)
    result = hashlib.md5(user.encode())
    result = result.hexdigest()
    print("MD5 hash ----->", result)

def sha256hash():
    user = str(input("Enter the text to Hash(SHA256 Hash):"))
    print("String ----->", user)
    result = hashlib.sha256(user.encode())
    result = result.hexdigest()
    print("SHA256 ----->", result)

def sha384hash():
    user = str(input("Enter the text to Hash(SHA384 Hash):"))
    print("String ----->", user)
    result = hashlib.sha384(user.encode())
    result = result.hexdigest()
    print("SHA384 ----->", result)

def sha224hash():
    user = str(input("Enter the text to Hash(SHA224 Hash):"))
    print("String ----->", user)
    result = hashlib.sha224(user.encode())
    result = result.hexdigest()
    print("SHA224 ----->", result)

def sha512hash():
    user = str(input("Enter the text to Hash(SHA512 Hash):"))
    print("String ----->", user)
    result = hashlib.sha512(user.encode())
    result = result.hexdigest()
    print("SHA512 ----->", result)

def sha1hash():
    user = str(input("Enter the text to Hash(SHA-1 Hash):"))
    print("String ----->", user)
    result = hashlib.sha1(user.encode())
    result = result.hexdigest()
    print("SHA-1 ----->", result)
#The menu choose a hash to encode

print("\nWelcome to TEXT2HASH CONVERTER !\n\nSELECT A HASH ALGORITHM:")

print("""
|-----|------------------------|
|Sl.no|  A L G O R I T H M S   |
|-----|------------------------|
|1 .  | MD5 Hash algorithm     |
|2 .  | SHA256 Hash algorithm  |
|3 .  | SHA384 Hash algorithm  |
|4 .  | SHA224 Hash algorithm  |
|5 .  | SHA512 Hash algorithm  |
|6 .  | SHA-1 Hash algorithm   |
|------------------------------|
""")

#We do a text input called

menu = str(input("select by number >>>>>>"))

#We use the if to create our options
if menu == "1":
    md5hash()
elif menu == "2":
    sha256hash()
elif menu == "3":
    sha384hash()
elif menu == "4":
    sha224hash()
elif menu == "5":
    sha512hash()
elif menu == "6":
    sha1hash()
#If user press wrong number print wrong number and end program
else:
    print("Wrong number")
