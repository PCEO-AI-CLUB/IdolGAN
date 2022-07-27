import os
import cv2
import mediapipe as mp
from tqdm import tqdm

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


def crop_to_RF512Img_pair(path, img_list_path, HQ_output_path='HQ_512x512', LQ_output_path='LQ'):
    """
    Crop all images in img_list_path to 512x512. All images will contain a face in the center.
    If face in the image has low resolution than 512x512, it will save to LQ_output_path folder.
    Else it will save to HQ_output_path folder.
    If the image does not contain a face, it will be skipped.

    :param path: path to the folder to save the cropped images
    :param img_list_path: list of paths to the images
    :param HQ_output_path: name of the folder to save the HQ images
    :param LQ_output_path: name of the folder to save the LQ images
    """
    if not os.path.exists(path + '/' + HQ_output_path):
        os.mkdir(path + '/' + HQ_output_path)

    if not os.path.exists(path + '/' + LQ_output_path):
        os.mkdir(path + '/' + LQ_output_path)

    # read,crop,save img
    for i, image_path in enumerate(tqdm(img_list_path)):
        image = cv2.imread(image_path)
        image = face_crop(image)
        if image is not None:
            try:
                h, w, _ = image.shape
                if h >= 512 or w >= 512:
                    image = cv2.resize(image, (512, 512), interpolation=cv2.INTER_LANCZOS4)
                    cv2.imwrite(path + "/" + HQ_output_path + "/" + str(i) + ".jpg", image,
                                [int(cv2.IMWRITE_JPEG_QUALITY), 100])  # HQ_image 512
                elif h > 0 and w > 0:
                    image = cv2.resize(image, (512, 512), interpolation=cv2.INTER_LANCZOS4)
                    cv2.imwrite(path + "/" + LQ_output_path + "/" + str(i) + ".jpg", image,
                                [int(cv2.IMWRITE_JPEG_QUALITY), 100])  # LQ_image below 512
            except:
                pass


def face_crop(image):
    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        if image is None:
            return None
        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        if not results.detections:
            # print("Face not found in image")
            return None
        # else:
        # print('Found {} faces.'.format(len(results.detections)))

        bounding_box = results.detections[0].location_data.relative_bounding_box  # just use primary face
        h, w, _ = image.shape

        X = int(w * bounding_box.xmin)
        Y = int(h * bounding_box.ymin)
        crop_img = image[Y:Y + int(h * bounding_box.height), X:X + int(w * bounding_box.width), :]
        return crop_img
