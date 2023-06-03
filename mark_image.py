from google.cloud import vision
import io


def markImage(file_name : str):
    client = vision.ImageAnnotatorClient.from_service_account_json('./keyfile.json')
    with io.open('./' + file_name, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    return labels[0].description
