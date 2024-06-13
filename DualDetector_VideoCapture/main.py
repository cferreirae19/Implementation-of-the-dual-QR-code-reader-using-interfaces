from qr_code_detector_v1 import QRCodeDetectorV1    # QReader
from qr_code_detector_v2 import QRCodeDetectorV2    # OpenCV
import cv2
import time

# Choose which detector to use
qr_code_detector = QRCodeDetectorV1()
#qr_code_detector = QRCodeDetectorV2()

# Open the camera
capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Couldn't open the camera")
    exit()
    
# Variables for FPS calculation
fps_start_time = time.time()
fps_counter = 0
fps_label = ''
    
while True:
    # Capture every frame
    ret, frame = capture.read()
    
    if not ret:
        print("Couldn't read a frame")
        break
    
    # Calculate FPS
    fps_counter += 1
    if time.time() - fps_start_time >= 1:
        fps = fps_counter / (time.time() - fps_start_time)
        fps_label = 'FPS: %.2f' % fps
        fps_counter = 0
        fps_start_time = time.time()
        
    cv2.putText(frame, fps_label, (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    qr_code_detector.detect_and_decode(frame)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()
