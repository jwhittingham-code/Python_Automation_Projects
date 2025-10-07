import os

update = os.system('apt update')
print("app list updated")
upgrade = os.system('apt upgrade')
print("updates installed")

