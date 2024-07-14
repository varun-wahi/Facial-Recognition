import cv2
import face_recognition

#Load known face encodings and names
known_face_encodings = []
known_face_names = []

# Load known faces and their names
known_person1_image = face_recognition.load_image_file("varun.jpg")
known_person2_image = face_recognition.load_image_file("shah_rukh_khan.jpg")
known_person3_image = face_recognition.load_image_file("chiku.jpg")

known_person1_encoding = face_recognition.face_encodings(known_person1_image)[0]
known_person2_encoding = face_recognition.face_encodings(known_person2_image)[0]
known_person3_encoding = face_recognition.face_encodings(known_person3_image)[0]

known_face_names.append("Varun Wahi")
known_face_names.append("Shah Rukh Khan")
known_face_names.append("Soumyadeep")

#Initialize webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    #Find all face locations
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    #Loop through each found face
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        #Check if the face matches any known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        
        #Draw a box around the face and label with name
        cv2.rectangle(frame, (left, top), (right, bottom), (0,0,255),2)
        cv2. putText(frame, name, (left, top - 10), cv2. FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    #Display the resulting frame
    cv2.imshow("Video", frame)

    #Break the loop when  q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#Release the webcam and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()




