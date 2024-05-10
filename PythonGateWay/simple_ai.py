from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_model.h5", compile=False)

# Load the labels
labels = open("labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)
# camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter('M', 'J', 'P', 'G'));

def image_detector():
    # Grab the webcamera's image.
    ret, image = camera.read()

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the image in a window
    cv2.imshow("Webcam Image", image)

    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Have the model predict what the current image is. Model.predict 
    # returns an array of percentages. Example: [0.2, 0.8] meaning its 20% sure
    # it is the first label and 80% sure its the second label.
    probabilities = model.predict(image)

    # Print what the highest value probabilitie label
    # print(labels[np.argmax(probabilities)])
    # print("Class:", class_name[2:], end="")
    # print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    # Listen to the keyboard for presses.
    cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    # if keyboard_input == 27:
        # break
    return labels[np.argmax(probabilities)]
# camera.release()
# cv2.destroyAllWindows()