import cv2
from interface import QRCodeDetector
from qreader import QReader
import time

class QRCodeDetector_QReader(QRCodeDetector):
    def __init__(self):
        self.qreader = QReader(model_size='n')  # Also tested with model_size='s'
        self.last_detection_times = {}

    def detect_and_decode(self, frame):
        current_time = time.time()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        decoded_texts = self.qreader.detect_and_decode(image=image, return_detections=True)

        if len(decoded_texts[0]) != 0:
            for decoded_text, detection in zip(decoded_texts[0], decoded_texts[1]):
                bounding_box = detection['bbox_xyxy']
                start_point = (int(bounding_box[0]), int(bounding_box[1]))
                end_point = (int(bounding_box[2]), int(bounding_box[3]))
                
                # Width, height and area of the bounding box
                width = abs(start_point[0] - end_point[0])
                height = abs(start_point[1] - end_point[1])
                area = width * height
                
                # Label showing the bounding box size
                dimensions_label = 'Size: %d x %d = %d' % (width, height, area)
                cv2.putText(frame, dimensions_label, (start_point[0], start_point[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
                cv2.rectangle(frame, start_point, end_point, (255, 0, 255), 3)
                
                # Print QR code data if 5 seconds have passed since the last detection
                if decoded_text not in self.last_detection_times or current_time - self.last_detection_times[decoded_text] > 5:
                    self.last_detection_times[decoded_text] = current_time
                    print("QR data: ", decoded_text)
        
        cv2.imshow("Detect QR Code from Webcam", frame)
        
        return decoded_texts
