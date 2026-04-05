import cv2

image_path = input("Enter image file name: ")

img = cv2.imread(image_path)

if img is None:
    print("Image not loaded")
    exit()

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.05,
    minNeighbors=3,
    minSize=(20,20)
)

print(f"Found {len(faces)} face(s)")

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)

cv2.imshow("Detected Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()