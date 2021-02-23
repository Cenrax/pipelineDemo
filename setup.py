from pipeline import Pipeline
import argparse
import os

if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--sourcePath", help = "Destination for the input folder")
    parser.add_argument("-d","--destinationPath", help = "Destination for the output folder")
    
    #We can add any more arguments as per our need including the sampling rate, hop length and eventually we can create a customizable menu 
    args = parser.parse_args()

    ## when the user fails to give the destination folder
    if(args.destinationPath == None): 
        defaultPath = os.path.join(os.path.abspath(os.getcwd()),"extractedFeatures/")
        if (not(os.path.exists(defaultPath))):
            os.makedirs(defaultPath)
        args.destinationPath = defaultPath
    
    ## when the destination folder does not exist
    if(not(os.path.exists(args.destinationPath))):
        os.makedirs(args.destinationPath)

    Pipeline = Pipeline(args.sourcePath,args.destinationPath) #we can pass the other arguments here. For now it assuming the default values
    Pipeline.extractMFCCFeatures()
    Pipeline.extractMELFeatures()