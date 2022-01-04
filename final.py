import os
os.system("npm install -g npm")
os.system("npm install -g localtunnel")
os.system("npm i --package-lock-only")
os.system("npm audit fix")
os.system("lt -p 5000 -s grahamswebsite")
