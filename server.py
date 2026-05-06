import io
from flask import Flask, Response
from picamera2 import Picamera2

app = Flask(__name__)
cam = Picamera2()

# Configure the camera's resolution
config = cam.create_preview_configuration(main={"size": (640, 480)})
cam.configure(config)
cam.start()

def generate_frames():
    while True: 
        # Capture frame into memory buffer
        stream = io.BytesIO()
        cam.capture_file(stream, format='jpeg')
        yield (b'--frame\r\n'b'Content-Type: image/jped\r\n\r\n' + stream.getvalue() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    # Return stream response
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    # Simple landing page
    return "<h1>Pi Camera Live Stream</h1><img src='/video_feed'>"

if __name__ == '__main__':
    # Run server
    app.run(host='0.0.0.0', port=5000, threaded=True)
