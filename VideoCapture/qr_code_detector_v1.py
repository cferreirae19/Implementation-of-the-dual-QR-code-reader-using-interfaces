import cv2
from interface import QRCodeDetector
from qreader import QReader

class QRCodeDetectorV1(QRCodeDetector):
    def __init__(self):
        self.qreader = QReader(model_size='n')

    def detect_and_decode(self, frame,):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        decoded_text = self.qreader.detect_and_decode(image=image, return_detections=True)
        
        if len(decoded_text[0]) != 0:
            bbox = decoded_text[1][0]['bbox_xyxy']
            start_point = (int(bbox[0]), int(bbox[1]))
            end_point = (int(bbox[2]), int(bbox[3]))
            w = abs(start_point[0]-end_point[0])
            h = abs(start_point[1]-end_point[1])
            a = w*h
            # Draw size (pixels)
            label = 'Size: %d x %d = %d' % (w,h,a)
            cv2.putText(frame, label, (0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.rectangle(frame, start_point, end_point, (255, 0, 255), 3)
            
        cv2.imshow("Detect QR Code from Webcam", frame)
        
        return decoded_text
