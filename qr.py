import segno

y = segno.make_qr("https://chat.openai.com/")
y.save("hEILLO.PNG")

import qrcode

x=qrcode.make('link')
x.save('hii.png')