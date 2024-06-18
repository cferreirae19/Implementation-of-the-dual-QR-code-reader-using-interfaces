import os
import time
import cv2
from qr_code_detector_qreader import QRCodeDetector_QReader
from qr_code_detector_opencv import QRCodeDetector_OpenCV

def get_image_files(directory):
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.lower().endswith(supported_formats)]

def process_images(detectors, image_files, log_file):
    with open(log_file, 'w') as log:
        dummy_image_file = image_files[0]  # Select the first image as the dummy image
        dummy_img = cv2.imread(dummy_image_file)
        
        # Process the dummy image with all detectors and discard the results
        if dummy_img is not None:
            for detector in detectors.values():
                try:
                    _ = detector.detect_and_decode(dummy_img.copy())
                except Exception as e:
                    print(f"Error processing dummy image: {str(e)}")

        # Process the remaining images
        for image_file in image_files[1:]:
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
    image_directory = './Test_QR_Codes'
    log_file = 'qr_code_detection_results.txt'

    detectors = {
        'QReader': QRCodeDetector_QReader(),
        'OpenCV': QRCodeDetector_OpenCV()
    }

    image_files = get_image_files(image_directory)
    
    if image_files:
        process_images(detectors, image_files, log_file)
        print(f"Results have been logged to {log_file}")
    else:
        print(f"No images found in {image_directory}")

if __name__ == "__main__":
    main()
