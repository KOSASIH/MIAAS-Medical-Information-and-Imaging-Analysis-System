import cv2
import numpy as np
from fastapi import APIRouter, HTTPException
from PIL import Image

router = APIRouter(prefix="/image-analysis", tags=["Image Analysis"])


@router.post("/object-detection")
async def object_detection(image: Image):
    # Convert image to OpenCV format
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Load YOLO model
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

    # Get image dimensions
    (H, W) = image_cv.shape[:2]

    # Define the layers
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # Construct a blob from the image
    blob = cv2.dnn.blobFromImage(
        image_cv, 1 / 255.0, (416, 416), swapRB=True, crop=False
    )

    # Pass the blob through the network
    net.setInput(blob)
    outputs = net.forward(ln)

    # Initialize the list of detected objects
    objects = []

    # Loop over the detections
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > 0.5 and classID == 0:
                # Extract the bounding box coordinates
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")

                # Update the list of detected objects
                objects.append(
                    {
                        "class": "person",
                        "confidence": confidence,
                        "bounding_box": {
                            "x": centerX,
                            "y": centerY,
                            "width": width,
                            "height": height,
                        },
                    }
                )

    return {"objects": objects}


@router.post("/image-classification")
async def image_classification(image: Image):
    # Load the image classification model
    model = tf.keras.models.load_model("image_classification_model.h5")

    # Preprocess the image
    image_array = np.array(image)
    image_array = image_array / 255.0
    image_array = image_array.reshape((1, 224, 224, 3))

    # Make predictions
    predictions = model.predict(image_array)

    # Get the top-5 predictions
    top_5_predictions = np.argsort(predictions[0])[-5:]

    # Return the top-5 predictions
    return {
        "predictions": [
            {"class": class_names[i], "confidence": predictions[0][i]}
            for i in top_5_predictions
        ]
    }
