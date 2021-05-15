import base64, uuid
from django.core.files import base
from django.core.files.base import ContentFile

def get_report_image(data):
    _ , str_image = data.split(';base64')
    decoded_img = base64.b64decode(str_image)
    img_name = str(uuid.uuid4())[:10] + '.png'
    data = ContentFile(decoded_img, name=img_name)
    return data





    # print(f)
    # print(str_image)
    # data:image/png