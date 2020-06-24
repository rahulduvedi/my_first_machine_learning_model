import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("image.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(gray,1.2,4)
for (x,y,w,z) in face:
    cv2.rectangle(img,(x,y),(x+w,y+z),(225,0,0),2)
cv2.imshow("img",img)
cv2.waitKey()
cv2.imwrite("image.jpg", img)
roi_color = img[y:y + h, x:x + w] 
print("[INFO] Object found. Saving locally.") 
cv2.imwrite(str(w) + str(h) + '_face.jpg', roi_color) 
