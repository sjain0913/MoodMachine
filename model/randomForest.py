import librosa
from librosa import display
import os
import warnings
import matplotlib.pyplot as plt
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 10)

randomForest = RandomForestClassifier(criterion = "gini", max_depth = 12, max_features = "log2", max_leaf_nodes = 100, min_samples_leaf = 3, min_samples_split = 20, n_estimators = 21000, random_state = 10)
randomForest.fit(X_train, y_train)

prediction = randomForest.predict(X_test)

## Result Reporting
print(classification_report(y_test, prediction))

            
