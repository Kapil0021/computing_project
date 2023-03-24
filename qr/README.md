
###################################GENERATE-QR######################

import pyqrcode
import datetime

#get current time
currentTime= datetime.datetime.now()
#add 10 seconds to current time
currentTimeWithBuffer = currentTime + datetime.timedelta(0,10)
#print the time
print(currentTime,"-",currentTimeWithBuffer)

currentTimeWithBufferStr = str(currentTimeWithBuffer)

#Account Number
accountNumber = '108000'
#Device to make sure the transaction availablity
transactionState='True'

qr_data=currentTimeWithBufferStr + '||' + accountNumber+ '||' + transactionState
#print the time
print(qr_data)

url = pyqrcode.create(qr_data)
#save the png file naming "qr.png"
url.png('qr//qr.png', scale = 6)


#####################READ-QR#########################

import cv2


# read the qr image
img = cv2.imread('qr//qr.png')

# initialize the cv2 qr detector
detector = cv2.QRCodeDetector()

# detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)

if bbox is not None:
    print(f"QRCode data: {data}")


