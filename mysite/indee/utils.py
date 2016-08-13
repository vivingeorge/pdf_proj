import os,string


# expects doc_path to start without /
def get_image_path_for_doc(doc_path):
    image_path = string.replace(doc_path, "documents", "doc_images")
    image_path = string.rsplit(image_path, ".pdf", 1)
    return image_path[0]+".jpg"


def get_image_folder_for_doc(doc_path):
    current_folder = doc_path.rsplit("/", 1)[0]
    dest_folder = string.replace(current_folder, "documents", "doc_images")
    return dest_folder


def get_doc_path_for_image():
    document = Document.objects.last()
