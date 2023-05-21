import uvicorn
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import PIL.Image as Image
import ocr
import predict
import os

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def home():
    return {"info": "Nothing to see here"}


def write_file(file):
    # Create media folder if not exists
    if not os.path.exists("media"):
        try:
            os.mkdir("media")
        except OSError:
            print("Creation of the directory failed")
            return {"error": "Creation of the directory failed"}
    file_location = f"media/{file.filename}"
    with open(file_location, "wb+") as file_obj:
        file_obj.write(file.file.read())

    return file_location


@app.post("/hwrc/")
async def create_upload_file(file: UploadFile):
    file_location = write_file(file)
    predict_handwriting = predict.predict_character(file_location)
    print(predict_handwriting)
    return {"predicted_handwriting": f'{predict_handwriting}'}


@app.post("/ocr/")
async def create_upload_file(file: UploadFile):
    file_location = write_file(file)
    # image = Image.open(file_location)
    result = ocr.get_reader().readtext(file_location, detail=0)
    return {"ocr_text": f'{result}'}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
