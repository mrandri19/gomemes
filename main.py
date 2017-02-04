from flask import Flask, render_template, request

from PIL import ImageFont, Image, ImageDraw

import base64
from io import BytesIO


img = Image.open("go_template.jpg")

def write_on_image(text):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Go-Mono.ttf", 20)

    draw.text((410, 0), text, (0, 0, 0), font=font)

    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())

    return img_str

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template('index.html')

    text = request.form['text']
    if text == "" or text == None:
        return 'Text missing from form data', 400

    # Split the string in lists <= 32 chars
    text_tmp = []
    line_tmp = ""
    counter = 0
    for char in text:
        if counter < 32:
            line_tmp += char
            counter += 1
        else:
            text_tmp.append(line_tmp)
            line_tmp = char
            counter = 1

    text_tmp.append(line_tmp)
    line_tmp = ""
    counter = 0

    # Join them with a newline
    text = "\n".join(text_tmp)
    # 8x32 monospace go-mono.ttf with size 20

    image_str = write_on_image(text).decode()
    return render_template('image.html', data=image_str)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
