import os
import time
import cv2
from qr_code_detector_v1 import QRCodeDetectorV1  # QReader
from qr_code_detector_v2 import QRCodeDetectorV2  # OpenCV

def get_image_files(directory):
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.lower().endswith(supported_formats)]

def process_images(detectors, image_files, log_file):
    with open(log_file, 'w') as log:
        for image_file in image_files:
            img = cv2.imread(image_file)
            if img is None:
                print(f"Error: Image {image_file} not loaded.")
                log.write(f"Image: {image_file}\n")
                log.write("  Error: Image not loaded.\n\n")
                continue
            
            log.write(f"Image: {image_file}\n")
            for detector_name, detector in detectors.items():
                try:
                    start_time = time.time()
                    decoded_results = detector.detect_and_decode(img.copy())
                    end_time = time.time()
                    elapsed_time = end_time - start_time

                    log.write(f"  Detector: {detector_name}\n")
                    log.write(f"    Execution time: {elapsed_time:.4f} seconds\n")
                    
                    if decoded_results:
                        for result in decoded_results:
                            if detector_name == 'QReader':
                                qr_data, width, height, area = result
                                log.write(f"    QR Code found. Size: {width} x {height} = {area} pixels\n")
                                log.write(f"    QR Code data: {qr_data}\n")
                            elif detector_name == 'OpenCV':
                                qr_data, (width, height, area) = result
                                log.write(f"    QR Code found. Size: {width} x {height} = {area} pixels\n")
                                log.write(f"    QR Code data: {qr_data}\n")
                    else:
                        log.write("    No QR Code found.\n")
                except Exception as e:
                    log.write(f"  Error: {str(e)}\n")
            log.write("\n")

def main():
    image_directory = './Test_QR_Codes'  # Current directory or specify your image directory here
    log_file = 'qr_code_detection_results.txt'

    detectors = {
        'QReader': QRCodeDetectorV1(),
        'OpenCV': QRCodeDetectorV2()
    }

    image_files = get_image_files(image_directory)
    process_images(detectors, image_files, log_file)

    print(f"Results have been logged to {log_file}")

if __name__ == "__main__":
    main()
