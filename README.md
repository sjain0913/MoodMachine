# MoodMachine

## Introduction
  Speech emotion recognition has many practical use cases in medicine, customer service and recommendation systems. We will implement our system using a variety of tools and machine learning libraries in Python. We will use soundfile for reading in audio files, librosa for extracting speech features, scikit-learn for model training, testing and validation, along with numpy, pickle and PyAudio. We will use a variety of models to determine the one with highest accuracy to map audio files to the correct emotions.
  
  For initial model training and analysis, we will use the RAVDESS dataset, which contains 7000+ files from 24 different actors speaking with varying moods (neutral, calm, happy, sad, angry, fearful, disgust, surprised). Each expression is produced at two levels of emotional intensity for better model training. Once our group has successfully built the model, we will create a training dataset with our own voice recordings and train another model using the same process. We will analyze the accuracy differences between the RAVDESS dataset model and our personal dataset model and draw results. Our project will produce a model capable of predicting emotions correctly through our own personalized dataset.
  
  After implementation, we used 4,948 files from the RAVDESS dataset. Out of the 7000+ files, we had to disregard the ones that were video only and had no audio. Since we are classifying emotions through audio analysis, these files have no value for this project. Here is the breakdown for the large chunk of RAVDESS we utilized:
  - Song Audio (Audio Only) = 24 actors x 44 clips = 1,056 audio files
  - Speech Audio (Audio Only) = 24 * 60 = 1,440 audio files
  - Video Song & Speech (Audio and Video) = 2,452 files
  - TOTAL = 4,948 audio files

  The RAVDESS Dataset follows the following naming convention (consists of a 7-part number only identifier):
  - Modality (01 = full-AV, 02 = video-only, 03 = audio-only)
  - Vocal channel (01 = speech, 02 = song)
  - Emotion (01 = neutral, 02 = calm, 03 = happy, 04 = sad, 05 = angry, 06 = fearful, 07 = disgust, 08 = surprised)
  - Emotional intensity (01 = normal, 02 = strong)
  - Statement (01 = “Kids are talking by the door”, 02 = “Dogs are sitting by the door”)
  - Repetition (01 = 1st rep, 02 = 2nd rep)
  - Actor (01-24, odd = male, even = female)
  
  We also followed a special process using the ffmpeg library. This was used to extract the wav audio from the video files in the RAVDESS dataset. We looped through all the files in the dataset that had .mp4 as an extension and used the ffmpeg library to convert these files to wav files with 160 bitrate. After this process was done, we were ready to test and train different types of models!
  
## Potential Results and Discussion
  For my initial results, I expected high recognition rates for strong emotions, such as anger and sadness, as well as for neutral emotions. More ambiguous emotions, such as disgust and fear, were expected to be more difficult to recognize.
  
  We started out by using a simple random forest model. This produced results shown below:


<p align="center">
    <img width="50%" src="https://github.com/sjain0913/MoodMachine/blob/main/images/randomForest.png">
</p>

  As we can see here, the random forest produces an average f1-score of 0.75. This is an average score and leaves much to be desired in terms of accuracy of the model. An acceptable score needs to be over the 0.8 mark. Even though random forest models can be used for both regression and classification tasks, it is not a completely accurate model in this case.
 
  After this, I wanted to improve on the accuracy through a Decision Tree model. This produced better results than I expected.
  
  
<p align="center">
    <img width="50%" src="https://github.com/sjain0913/MoodMachine/blob/main/images/decisionTree.png">
</p>

  As we can see here, the decision tree produces an average f1-score of 0.82. This is an acceptable and good measure for the accuracy of the model and shows that the decision tree model is apt for this task. If I had more time, I would attempt training a neural network model for the same task.