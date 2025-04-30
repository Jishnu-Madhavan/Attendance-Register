import cv2
import face_recognition
import pickle
import os

# Importing the student images.
folderPath = 'Images'
PathList = [path for path in os.listdir(folderPath) if path.lower().endswith(('.png', '.jpg', '.jpeg'))]
print(PathList)

imgList = []
studentIds = []
for path in PathList:
    img = cv2.imread(os.path.join(folderPath, path))
    if img is not None:
        imgList.append(img)
        studentIds.append(os.path.splitext(path)[0])
    else:
        print(f"Warning: Unable to load image {path}")
print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for idx, img in enumerate(imagesList):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodes = face_recognition.face_encodings(img)
        if encodes:
            encodeList.append(encodes[0])
        else:
            print(f"Warning: No face found in image {studentIds[idx]}")
    return encodeList

print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

# Save the encodings to a file.
file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
