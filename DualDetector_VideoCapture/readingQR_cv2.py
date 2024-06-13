import cv2
import numpy as np
from pyzbar.pyzbar import decode

def detect_qr_codes(frame):
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find QR codes in the frame
    qr_codes = decode(gray_frame)

    return qr_codes
    
def extract_qr_data(qr_codes):
    if qr_codes:
        for qr_code in qr_codes:
            # Extract the data from the QR code
            qr_data = qr_code.data.decode('utf-8')
            print("QR Code Data:", qr_data)

def draw_qr_code_rectangles(frame, qr_codes):
    if qr_codes:
        for qr_code in qr_codes:
            # Draw a rectangle around the QR code on the frame
            points = qr_code.polygon
            rct = qr_code.rect
            w = rct[2]
            h = rct[3]
            a = w*h
            # Draw size (pixels)
            label = 'Size: %d x %d = %d' % (w,h,a)
            cv2.putText(frame, label, (0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            if len(points) > 4:
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                cv2.polylines(frame, [hull], True, (255, 0, 255), 3)
            else:
                cv2.polylines(frame, [np.array(points, dtype=np.int32)], True, (255, 0, 255), 3)
                
def detect_and_decode(frame):
    qr_codes = detect_qr_codes(frame)
    extract_qr_data(qr_codes)
    draw_qr_code_rectangles(frame, qr_codes)

    # Display the frame with detected QR codes
    cv2.imshow("Detect QR Code from Webcam", frame)