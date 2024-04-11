import pyqrcode

data = "https://www.buymeacoffee.com/deepeshkal4"


qr = pyqrcode.create(data)

print(qr.terminal(quiet_zone=1)) 
