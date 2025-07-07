# 07_qr_grabber.py
import qrcode

def generate_qr(data):
    img = qrcode.make(data)
    img.save("qr_code.png")
    print("✅ QR code enregistré sous : qr_code.png")

if __name__ == "__main__":
    text = input("Donnée à convertir en QR : ")
    generate_qr(text)
