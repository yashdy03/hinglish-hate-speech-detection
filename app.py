from flask import Flask, request, jsonify
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import regularizers
from tensorflow.keras import preprocessing
import numpy as np

app = Flask(__name__)
model = load_model('/home/mozart/yos/minor/minor2/lstmapi/lstm_model.h5')
# Set the maximum sequence length
MAX_SEQUENCE_LENGTH = 50
tokenizer = Tokenizer()
# Start the Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the text input from the POST request
    text = request.json['text']

    # Convert the text input into a padded sequence of integers
    tokens = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(tokens, maxlen=MAX_SEQUENCE_LENGTH)

    # Make the prediction using the LSTM model
    prediction = model.predict(padded_sequence)

    # Format the prediction as a dictionary and return it as a JSON response
    prediction_dict = {'prediction': int(np.round(prediction))}
    return jsonify(prediction_dict)

if __name__ == '__main__':
    app.run(debug=True)

