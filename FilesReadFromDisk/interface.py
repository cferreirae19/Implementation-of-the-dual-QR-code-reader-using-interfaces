from abc import ABC, abstractmethod

class QRCodeDetector(ABC):
    @abstractmethod
    def detect_and_decode(self, frame):
        pass