import os

class VisionProvider:
    def analyze_image(self, image_path: str, prompt: str) -> str:
        raise NotImplementedError

class LocalMockVisionProvider(VisionProvider):
    def analyze_image(self, image_path: str, prompt: str) -> str:
        if not os.path.exists(image_path):
            return "Image not found."
        filename = os.path.basename(image_path)
        return f"[Vision Analysis for {filename}]: Image appears to contain user query context related to '{prompt}'."

def get_vision_provider(provider_type="local_mock") -> VisionProvider:
    return LocalMockVisionProvider()
