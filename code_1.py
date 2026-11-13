import qrcode
url = "https://github.com/pakaiwela-arch/hbdselebbb.git"
img = qrcode.make(url)
img.save("qr_web.png")
print("QR code berhasil dibuat")