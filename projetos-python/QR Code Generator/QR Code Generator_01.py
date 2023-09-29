#QR Code Generator 01
#Not entirely mine
import qrcode

data = 'Don\'t forget to be cool'

img = qrcode.make(data)
img.save('C:/Users/Ceiça/Downloads/Sublime Text/Projects/QR Code Generator/qrcode_01.png')
