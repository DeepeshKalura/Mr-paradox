import pyqrcode




def generate_qr_code():
    data = "https://www.buymeacoffee.com/deepeshkal4"
    qr = pyqrcode.create(data)
    return qr.terminal(quiet_zone=1)
 
