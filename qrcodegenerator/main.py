import pyqrcode

data = "https://github.com/JoseAntonioIosephvsAnthonivs"

qr = pyqrcode.create(data)
qr.png("QRCODEGITHUB.png", scale=5)