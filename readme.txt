1) Install the required packages using pip Install -r requirements.txt

2) Extract the features by giving absolute input path using -s argument and absolute output path using -d argument.
If destination path is the code will make a default folder in the current directory

For example:

setup.py -s "G:/pipelineDemo/music_dataset/" -d "G:/pipeLineDemo/extractedFeatures/"

3) To run the unit test write python test_pipeline.py
