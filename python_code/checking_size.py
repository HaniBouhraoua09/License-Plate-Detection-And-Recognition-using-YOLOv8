import cv2

def video_size():
    # Open the video capture
    cap = cv2.VideoCapture("demo.mp4")  # Replace with your video file

    # Check if the video capture is successfully opened
    if not cap.isOpened():
       print("Error: Could not open video.")
       exit()

    # Get the dimensions of the video frames
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Print the dimensions
    print("Video Frame Dimensions:")
    print(f"Width: {width} pixels")
    print(f"Height: {height} pixels")

def img_size():
    # Read an image
    image = cv2.imread("your_image.jpg")  # Replace with your image file

    # Check if the image is successfully loaded
    if image is None:
       print("Error: Could not read the image.")
       exit()

    # Get the dimensions of the image
       height, width, channels = image.shape

    # Print the dimensions
    print("Image Dimensions:")
    print(f"Height: {height} pixels")
    print(f"Width: {width} pixels")
    print(f"Channels: {channels}")

# video_size()
# img_size()


