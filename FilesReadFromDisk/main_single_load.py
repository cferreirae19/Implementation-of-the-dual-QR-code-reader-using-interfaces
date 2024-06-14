from qr_code_detector_v1 import QRCodeDetectorV1  # QReader
from qr_code_detector_v2 import QRCodeDetectorV2  # OpenCV
import cv2

# Choose which detector to use
qr_code_detector = QRCodeDetectorV1()
#qr_code_detector = QRCodeDetectorV2()

img = cv2.imread("./Test_QR_Codes/TestCollage.png")

if img is not None:
    decoded_results = qr_code_detector.detect_and_decode(img)
    for result in decoded_results:
        qr_data, width, height, area = result
        print(f"QR Code found. Size: {width} x {height} = {area} pixels")
        print(f"QR Code data: {qr_data}")
else:
    print("Error: Image not loaded.")
