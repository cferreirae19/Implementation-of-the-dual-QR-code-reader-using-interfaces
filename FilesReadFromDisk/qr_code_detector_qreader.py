import cv2
from interface import QRCodeDetector
from qreader import QReader

class QRCodeDetector_QReader(QRCodeDetector):
    def __init__(self):
        self.qreader = QReader(model_size='n')

    def detect_and_decode(self, frame):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        decoded_texts = self.qreader.detect_and_decode(image=image, return_detections=True)

        results = []
        if len(decoded_texts[0]) != 0:
            for decoded_text, detection in zip(decoded_texts[0], decoded_texts[1]):
                bounding_box = detection['bbox_xyxy']
                start_point = (int(bounding_box[0]), int(bounding_box[1]))
                end_point = (int(bounding_box[2]), int(bounding_box[3]))
                
                width = abs(start_point[0] - end_point[0])
                height = abs(start_point[1] - end_point[1])
                area = width * height
                
                results.append((decoded_text, width, height, area))

        return results
