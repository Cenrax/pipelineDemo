import unittest
from pipeline import Pipeline

sourcePath = "G:/pipelineDemo/music_dataset/" #give your preferred source path to the database
destinationPath = "G:/pipelineDemo/extractedFeatures/" #give your preferred destination path for the output folder
pipeline = Pipeline(sourcePath,destinationPath)

class TestPipeline(unittest.TestCase):
    
    def test_extractMFCCFeatures(self):
        self.assertGreaterEqual(pipeline.extractMFCCFeatures(), 0) 
    
    def test_extractMELFeatures(self):
        self.assertGreaterEqual(pipeline.extractMELFeatures(), 0)

if __name__ == "__main__":
    unittest.main()
