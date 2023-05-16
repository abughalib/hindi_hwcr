from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
import numpy as np
import numpy as np
import cv2
import numpy as np

# Load model
model = load_model('model.h5')

transform = ImageDataGenerator(rescale=1./255)

kernel = np.ones((5, 5), np.uint8)

def predict_character(image_path):
    img = cv2.imread(image_path, 0)

    _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    img = cv2.dilate(img,kernel,iterations = 9)
    resized = cv2.resize(img, (32,32), interpolation = cv2.INTER_AREA)
    resized = resized.astype('float32')
    resized=resized/255
    resized = np.expand_dims(resized, axis=0)
    resized.shape = (-1,32,32,1)
    predict=model.predict(resized)
    char_index = np.argmax(predict)
    key_list = [
        'character_10_yna', 'character_11_taamatar', 'character_12_thaa', 
        'character_13_daa', 'character_14_dhaa', 'character_15_adna', 
        'character_16_tabala', 'character_17_tha', 'character_18_da', 
        'character_19_dha', 'character_1_ka', 'character_20_na', 'character_21_pa', 
        'character_22_pha', 'character_23_ba', 'character_24_bha', 'character_25_ma', 
        'character_26_yaw', 'character_27_ra', 'character_28_la', 'character_29_waw', 
        'character_2_kha', 'character_30_motosaw', 'character_31_petchiryakha', 
        'character_32_patalosaw', 'character_33_ha', 'character_34_chhya', 
        'character_35_tra', 'character_36_gya', 'character_3_ga', 'character_4_gha', 
        'character_5_kna', 'character_6_cha', 'character_7_chha', 'character_8_ja', 
        'character_9_jha', 'digit_0', 'digit_1', 'digit_2', 'digit_3', 'digit_4', 
        'digit_5', 'digit_6', 'digit_7', 'digit_8', 'digit_9'
        ]
    char = key_list[char_index]
    characters = {
        'character_1_ka': 'क',
        'character_2_kha': 'ख',
        'character_3_ga': 'ग',
        'character_4_gha': 'घ',
        'character_5_kna': 'ङ',
        'character_6_cha': 'च',
        'character_7_chha': 'छ',
        'character_8_ja': 'ज',
        'character_9_jha': 'झ',
        'character_10_yna': 'ञ',
        'character_11_taamatar': 'ट',
        'character_12_thaa': 'ठ',
        'character_13_daa': 'ड',
        'character_14_dhaa': 'ढ',
        'character_15_adna': 'ण',
        'character_16_tabala': 'त',
        'character_17_tha': 'थ',
        'character_18_da': 'द',
        'character_19_dha': 'ध',
        'character_20_na': 'न',
        'character_21_pa': 'प',
        'character_22_pha': 'फ',
        'character_23_ba': 'ब',
        'character_24_bha': 'भ',
        'character_25_ma': 'म',
        'character_26_yaw': 'य',
        'character_27_ra': 'र',
        'character_28_la': 'ल',
        'character_29_waw': 'व',
        'character_30_motosaw': 'श',
        'character_31_petchiryakha': 'ष',
        'character_32_patalosaw': 'स',
        'character_33_ha': 'ह',
        'character_34_chhya': 'क्ष',
        'character_35_tra': 'त्र',
        'character_36_gya': 'ज्ञ',
        'digit_0': '०',
        'digit_1': '१',
        'digit_2': '२',
        'digit_3': '३',
        'digit_4': '४',
        'digit_5': '५',
        'digit_6': '६',
        'digit_7': '७',
        'digit_8': '८',
        'digit_9': '९'
    }
    
    return characters[char]


if __name__ == '__main__':
    print(predict_character('media/2.jpg'))