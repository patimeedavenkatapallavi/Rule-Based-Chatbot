import cv2

image_path = input("Enter image file name: ")

img = cv2.imread(image_path)

if img is None:
    print("Image not loaded")
    exit()

print("Image Loaded Successfully")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30,30)
)

print(f"Found {len(faces)} face(s)")

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)

# Fix display issue
h, w = img.shape[:2]
img = cv2.resize(img, (w//2, h//2))

cv2.namedWindow("Detected Faces", cv2.WINDOW_NORMAL)
cv2.imshow("Detected Faces", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
