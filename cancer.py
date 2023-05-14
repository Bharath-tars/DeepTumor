import tensorflow as tf
import numpy as np
import cv2


def detect_cancer(image_path,name):
    # Load trained model and weights
    model = tf.keras.models.load_model('model.h5')
    model.load_weights('weights.h5')

    # Load and preprocess image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (224, 224))
    image = np.expand_dims(image, axis=-1)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0

    # Predict cancer possibility
    prediction = model.predict(image)
    cancer_possibility = prediction[0][0] * 100

    # Detect tumor content
    # TODO: Add code to detect tumor content

    # Generate report
    report = f"Dear {name},\n\nThank you for using DeepTumor for cancer detection. The results of your cancer test are:\n\nCancer Possibility: {cancer_possibility:.2f}%\n\nPlease find attached the detailed cancer detection report.\n\nBest regards,\nDeepTumor Team"

    return report
