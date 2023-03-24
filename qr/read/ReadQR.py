import cv2


# read the qr image
img = cv2.imread('qr.png')

# initialize the cv2 qr detector
detector = cv2.QRCodeDetector()

# detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)

if bbox is not None:
    print(f"QRCode data: {data}")