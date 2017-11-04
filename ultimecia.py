import cv2
import sys
import skvideo.io
# vidcap = cv2.VideoCapture('foo.mkv')
vidcap = skvideo.io.VideoCapture('foo.mkv')
success = True
count = 1
success, image = vidcap.read()
resulting_image = image
print(resulting_image)
while success and count < 15000:
  print("Processing frame ", count)
  resulting_image = (resulting_image * count + image)/(count + 1)
  print(resulting_image[0][0])
  count += 1
  success, image = vidcap.read()

cv2.imwrite("foo", resulting_image)
