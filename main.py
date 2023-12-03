from os import remove
from uuid import uuid4

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from PIL import Image, ImageDraw
from pydantic import BaseModel
from starlette.background import BackgroundTask
from starlette.responses import FileResponse


class ImageData(BaseModel):
    strokes: list
    box: list


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/transform")
async def transform(image_data: ImageData):
    filepath = "./images/" + str(uuid4()) + ".png"
    img = transform_img(image_data.strokes, image_data.box)
    img.save(filepath)

    return FileResponse(filepath, background=BackgroundTask(remove, path=filepath))


app.mount("/", StaticFiles(directory="static", html=True), name="static")


def transform_img(strokes, box):
    # Calc cropped image size
    width = box[2] - box[0]
    height = box[3] - box[1]

    image = Image.new("RGB", (width, height), color=(255, 255, 255))
    image_draw = ImageDraw.Draw(image)

    for stroke in strokes:
        positions = []
        for i in range(0, len(stroke[0])):
            positions.append((stroke[0][i], stroke[1][i]))
        image_draw.line(positions, fill=(0, 0, 0), width=3)

    return image.resize(size=(28, 28))
