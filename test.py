import numpy as np
import tensorflow as tf
import librosa

# Load the trained model
model = tf.keras.models.load_model('Models/Trained Model/202402151720/model.h5')

# Compile the model with CTC loss
optimizer = tf.keras.optimizers.Adam()
model.compile(optimizer=optimizer, loss=tf.nn.ctc_loss, metrics=['accuracy'])

# Function to preprocess audio files
def preprocess_audio(audio_path):
    # Load the audio file
    audio, _ = librosa.load(audio_path, sr=16000)
    # Apply the same preprocessing used during training
    # For example: convert to MFCC features
    mfccs = librosa.feature.mfcc(y=audio, sr=16000, n_mfcc=40)
    # Normalize the features
    mfccs_normalized = np.mean(mfccs.T,axis=0)
    # Expand dimensions to match the shape expected by the model
    mfccs_expanded = np.expand_dims(mfccs_normalized, axis=0)
    return mfccs_expanded

# Function to perform speech recognition
def recognize_speech(audio_path):
    # Preprocess the audio
    processed_audio = preprocess_audio(audio_path)
    # Perform inference using the model
    predictions = model.predict(processed_audio)
    # Get the index of the predicted class
    predicted_index = np.argmax(predictions)
    # Map the index to the corresponding label (if you have labels)
    # Otherwise, you might need a separate mapping from index to words
    labels = ["word1", "word2", "word3"]  # Example labels
    predicted_label = labels[predicted_index]
    return predicted_label

# Example usage
audio_path = 'Datasets/LJSpeech-1.1/wavs/myvoice22.wav'
result = recognize_speech(audio_path)
print("Predicted word:", result)