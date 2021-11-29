import librosa
from librosa import display
import os
import warnings
import matplotlib.pyplot as plt
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import pickle

warnings.filterwarnings("ignore")

data, samplingRate = librosa.load('./model/RAVDESS/Audio_Speech_Actors_01-24/Actor_01/03-01-01-01-01-01-01.wav')
plt.figure(figsize = (12, 4))
librosa.display.waveplot(data, sr=samplingRate)

datasetPath = "./model/RAVDESS"
fileList = []

for subdir, dirs, files in os.walk(datasetPath):
    for file in files:
        if file.endswith('.wav'):
            try:
                X, sampleRate = librosa.load(os.path.join(subdir, file), res_type='kaiser_fast')
                mfcc = np.mean(librosa.feature.mfcc(y = X, sr = sampleRate, n_mfcc = 40).T, axis = 0)
                file = file[6:8]
                temp = mfcc, file
                fileList.append(temp)
            except ValueError:
                print(ValueError)
                continue
        
X, y = zip(*fileList)
X = np.asarray(X)
y = np.asarray(y)
print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 10)

decisionTree = DecisionTreeClassifier()
decisionTree.fit(X_train, y_train)

modelFilename = "decisionTreeModel.pkl"
pickle.dump(decisionTree, open(modelFilename, 'wb'))

prediction = decisionTree.predict(X_test)

savedModel = pickle.load(open(modelFilename, 'rb'))
savedPrediction = savedModel.predict(X_test)

## Result Reporting
print("Report for Live Model")
print(classification_report(y_test, prediction))

print("Report for Saved Model")
print(classification_report(y_test, savedPrediction))

            
