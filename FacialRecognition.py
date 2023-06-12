# Jeremy Pretty Basic Facial Recognition
import PIL.ImageDraw
import face_recognition
import os

# Path to the File
face_picture = os.path.join(os.path.dirname(__file__), 'GroupOfPeople1.jpg')

# Load the image file into a numpy array
faces = face_recognition.load_image_file(face_picture)

# Find all the faces in the image
faceLocations = face_recognition.face_locations(faces)

# Get the number of faces found
numberOfFaces = len(faceLocations)
print("Found {} face(s) in this picture.".format(numberOfFaces))

# Load the image into a PIL Image object to draw on it
pilImage = PIL.Image.fromarray(faces)

# Loop through each face location and draw a red box around it
for faceLocation in faceLocations:
    # Extract the coordinates of the face location
    top, right, bottom, left = faceLocation

    # Print the location of each face
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # Draw a box around the face
    drawHandle = PIL.ImageDraw.Draw(pilImage)
    drawHandle.rectangle([left, top, right, bottom], outline="red")

# Display the image with the face boxes
pilImage.show()
