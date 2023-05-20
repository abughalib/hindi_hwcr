import easyocr

reader = easyocr.Reader(['hi'])

def get_reader():
    return reader