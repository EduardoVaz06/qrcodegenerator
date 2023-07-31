import qrcode
import image

qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('www.youtube.com')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("test.png")
