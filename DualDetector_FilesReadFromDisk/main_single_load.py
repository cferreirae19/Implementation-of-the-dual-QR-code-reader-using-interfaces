from qr_code_detector_v1 import QRCodeDetectorV1  # QReader
from qr_code_detector_v2 import QRCodeDetectorV2  # OpenCV
import cv2

# Choose which detector to use
#qr_code_detector = QRCodeDetectorV1()
qr_code_detector = QRCodeDetectorV2()

# Load the image from memory
img = cv2.imread("TestImage5.jpg")

# Ensure the image is loaded
if img is not None:
    cv2.imshow("Detect QR Code from Webcam", img)
    qr_code_detector.detect_and_decode(img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("Error: Image not loaded.")
