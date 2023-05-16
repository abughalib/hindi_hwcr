import uvicorn
from fastapi import FastAPI, UploadFile
import predict
import os

app = FastAPI()


@app.get("/")
async def home():
    return {"info": "Nothing to see here"}


@app.post("/upload_image/")
async def create_upload_file(file: UploadFile):
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

    predict_handwriting = predict.predict_character(file_location)
    print(predict_handwriting)
    return {"predicted_handwriting": f'{predict_handwriting}'}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
