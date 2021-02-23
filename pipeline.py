import os
import librosa
import argparse
import numpy as np
class Pipeline:

    def __init__(self, sourcePath, destinationPath , samplingRate = 22050, hopLength = 512, nFFT = 2048):
        self.sourcePath = sourcePath
        self.destinationPath = destinationPath
        self.samplingRate = samplingRate
        self.hopLength = hopLength
        self.nFFT = nFFT
    
    def getSourcePath(self):
        return(self.sourcePath)
        
    def getDestinationPath(self):
        return(self.destinationPath)

    def saveFeatures(self, path, dataArray):
        np.save(path,dataArray)

    def setSamplingRate(self,samplingRate):
        self.samplingRate = samplingRate

    def getSamplingRate(self):
        return (self.samplingRate)

    def setHopLength(self,hopLength):
        self.hopLength = hopLength

    def getHopLength(self):
        return (self.hopLength)

    def setnFFT(self,nFFT):
        self.nFFT = nFFT

    def getnFFT(self):
        return (self.nFFT)
    
    def extractMFCCFeatures(self):
        sourcePath = self.getSourcePath()
        destinationPath = self.getDestinationPath()
        datasetFolder = os.listdir(self.getSourcePath())
        samplingRate = self.getSamplingRate()
        hopLength = self.getHopLength()
        nFFT = self.getnFFT()
        for audioFile in datasetFolder:
            signal,sr = librosa.load(sourcePath+audioFile, sr = samplingRate)
            MFCCs = librosa.feature.mfcc(signal,samplingRate, n_fft=nFFT, hop_length=hopLength, n_mfcc=13)
            savedMfcc = os.path.join(destinationPath,audioFile.split('.')[0]+"_mfccs.npy")
            self.saveFeatures(savedMfcc,MFCCs)
        return (len(os.listdir(destinationPath)))
        
    def extractMELFeatures(self):
        sourcePath = self.getSourcePath()
        destinationPath = self.getDestinationPath()
        datasetFolder = os.listdir(self.getSourcePath())
        samplingRate = self.getSamplingRate()
        for audioFile in datasetFolder:
            signal,sr = librosa.load(sourcePath+audioFile, sr = self.samplingRate)
            mel = librosa.feature.melspectrogram(signal, self.samplingRate)
            savedMel = os.path.join(destinationPath,audioFile.split('.')[0]+"_mel.npy")
            self.saveFeatures(savedMel,mel)
        return len(os.listdir(destinationPath))




        