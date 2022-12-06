import os
os.system("clear")
os.system("apt update -y && apt upgrade -y")
os.system("pkg install mariadb -y")
print("RUN sql.py FILE")
