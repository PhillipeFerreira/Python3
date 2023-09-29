#QR Code Generator 02
#Not entirely mine
import qrcode

data = 'Don\'t forget to be cool'

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill_color = 'red', back_color = 'white')
img.save('C:/Users/Ceiça/Downloads/Sublime Text/Projects/QR Code Generator/qrcode_02.png')
