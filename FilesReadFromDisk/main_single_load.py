from qr_code_detector_qreader import QRCodeDetector_QReader  # QReader
from qr_code_detector_opencv import QRCodeDetector_OpenCV  # OpenCV
import cv2

# ===== Test with a single image =====

# Choose which detector to use
qr_code_detector = QRCodeDetector_QReader()
#qr_code_detector = QRCodeDetector_OpenCV()

img = cv2.imread("./Test_QR_Codes/TestCollage.png")

if img is not None:
    decoded_results = qr_code_detector.detect_and_decode(img)
    for result in decoded_results:
        qr_data, width, height, area = result
        print(f"QR Code found. Size: {width} x {height} = {area} pixels")
        print(f"QR Code data: {qr_data}")
else:
    print("Error: Image not loaded.")
