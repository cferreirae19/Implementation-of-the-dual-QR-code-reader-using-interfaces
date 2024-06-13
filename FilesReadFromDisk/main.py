import os
import time
import cv2
from qr_code_detector_v1 import QRCodeDetectorV1  # QReader
from qr_code_detector_v2 import QRCodeDetectorV2  # OpenCV

def get_image_files(directory):
    """
    Retrieve a list of image files from the specified directory.
    
    Args:
        directory (str): Path to the directory containing images.
        
    Returns:
        list: List of image file paths.
    """
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.lower().endswith(supported_formats)]

def process_images(detectors, image_files, log_file):
    """
    Process each image with the given detectors and log the results.
    
    Args:
        detectors (dict): Dictionary of detector names and instances.
        image_files (list): List of image file paths.
        log_file (str): Path to the log file for storing results.
    """
    with open(log_file, 'w') as log:
        for image_file in image_files:
            # Load the image
            img = cv2.imread(image_file)
            if img is None:
                print(f"Error: Image {image_file} not loaded.")
                log.write(f"Image: {image_file}\n")
                log.write("  Error: Image not loaded.\n\n")
                continue
            
            log.write(f"Image: {image_file}\n")
            for detector_name, detector in detectors.items():
                try:
                    # Measure the start time
                    start_time = time.time()
                    # Detect and decode QR codes
                    decoded_text = detector.detect_and_decode(img.copy())  # Use a copy to keep original image unaltered
                    # Measure the end time
                    end_time = time.time()
                    elapsed_time = end_time - start_time

                    log.write(f"  Detector: {detector_name}\n")
                    log.write(f"    Execution time: {elapsed_time:.4f} seconds\n")

                    if detector_name == 'QReader':
                        if decoded_text and len(decoded_text[0]) != 0:
                            bbox = decoded_text[1][0]['bbox_xyxy']
                            width = int(bbox[2] - bbox[0])
                            height = int(bbox[3] - bbox[1])
                            area = width * height
                            log.write(f"    QR Code found. Size: {width} x {height} = {area} pixels\n")
                        else:
                            log.write("    No QR Code found.\n")
                    elif detector_name == 'OpenCV':
                        # Check the return value from detect_and_decode
                        if decoded_text is not None:
                            width, height, area = decoded_text
                            log.write(f"    QR Code found. Size: {width} x {height} = {area} pixels\n")
                        else:
                            log.write("    No QR Code found.\n")
                except Exception as e:
                    log.write(f"  Error: {str(e)}\n")
            log.write("\n")

def main():
    """
    Main function to perform batch QR code detection on images in a directory.
    """
    image_directory = '.'  # Current directory or specify your image directory here
    log_file = 'qr_code_detection_results.txt'

    # Initialize detectors
    detectors = {
        'QReader': QRCodeDetectorV1(),
        'OpenCV': QRCodeDetectorV2()
    }

    # Get list of image files
    image_files = get_image_files(image_directory)

    # Process images with both detectors and log results
    process_images(detectors, image_files, log_file)

    print(f"Results have been logged to {log_file}")

    # Wait for user to close the images
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
