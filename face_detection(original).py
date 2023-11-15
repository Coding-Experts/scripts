import dlib
import numpy as np
import cv2

# Load the face detector, landmark predictor, and face recognition model
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_rec_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")


def get_face_descriptor(img_path):
    img = cv2.imread(img_path)
    if img is None:
        return None

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detect face
    dets = detector(img_rgb, 1)
    if len(dets) == 0:
        return None

    # Get landmarks
    shape = predictor(img_rgb, dets[0])

    # Get descriptor
    face_descriptor = face_rec_model.compute_face_descriptor(img_rgb, shape)

    return np.array(face_descriptor)


def are_faces_similar(desc1, desc2, threshold=0.6):
    if desc1 is None or desc2 is None:
        return False

    distance = np.linalg.norm(desc1 - desc2)
    return distance < threshold


# List of images to compare
image_paths = [f"img-{i}.jpeg" for i in range(1, 7)]
descriptors = [(path, get_face_descriptor(path)) for path in image_paths]

# Group images with similar descriptors
groups = []
for path, desc in descriptors:
    if desc is not None:
        matched = False
        for group in groups:
            if are_faces_similar(desc, descriptors[group[0]][1]):
                group.append(image_paths.index(path))
                matched = True
                break
        if not matched:
            groups.append([image_paths.index(path)])

for group in groups:
    if len(group) > 1:
        images = ", ".join([f"Image {i + 1}" for i in group])
        print(f"{images} are of the same person.")
