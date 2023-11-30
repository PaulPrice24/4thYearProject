import cv2
import mediapipe as mp
import pyautogui

# Open the camera
cam = cv2.VideoCapture(0)

# Initialize the face model
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Get the screen size using pyautogui
screen_w, screen_h = pyautogui.size()

# Main loop to continuously capture frames from the camera
while True:
    # Read a frame from the camera
    _, frame = cam.read()

    # Flip the frame
    frame = cv2.flip(frame, 1)

    # Convert the BGR frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the RGB frame with the FaceMesh model
    output = face_mesh.process(rgb_frame)

    # Extract facial landmark points from the output
    landmark_points = output.multi_face_landmarks

    # Get the height and width of the frame
    frame_height, frame_width, _ = frame.shape

    # Check if facial landmarks are detected
    if landmark_points:
        # Get the landmarks of the first face detected
        landmarks = landmark_points[0].landmark

        # Draw a circle on specific landmarks for visualization
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))

            # Move the mouse cursor to the specified landmark
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)

        # Extract left eye landmarks for additional visualization
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

        # Check if the left eye is closed based on y-coordinate difference
        if (left[0].y - left[1].y) < 0.004:
            # Simulate a mouse click if the eye is closed
            pyautogui.click()
            pyautogui.sleep(1)

    # Display the processed frame with the added visualizations
    cv2.imshow('Eye Tracker', frame)

    # Wait for a key event (1 millisecond delay)
    cv2.waitKey(1)