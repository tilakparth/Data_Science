import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")


ret, frame = cap.read()
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# cap.release()

# if ret == False:
# continue
faces = face_cascade.detectMultiScale

cv2.imshow("Video Frame", frame)
cv2.imshow("Gray Frame", gray_frame)


cap.release()
# cv2.waitKey(5000)
cv2.destroyAllWindows()

# for video
# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     if ret == False:
#         continue
#     cv2.imshow("Video Frame", frame)
#     cv2.imshow("Gray Frame", gray_frame)
#     key_presses = cv2.waitKey(1) & 0xFF
#     if key_presses == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
