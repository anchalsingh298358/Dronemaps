from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
import cv2
from report_generation import generate_pdf_report

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def detect_objects(video_path):
    global vid_data
    # Placeholder implementation of object detection using OpenCV
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    potholes_count = 0
    lane_markings_count = 0
    traffic_lights_count = 0
    signages_count = 0
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
        
        # Placeholder logic for object detection
        # Example: Counting objects based on color
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 100:
                potholes_count += 1  # Placeholder for potholes detection
        
        frame_count += 1
    
    cap.release()
    
    vid_data={
        'potholes': potholes_count,
        'lane_markings': lane_markings_count,
        'traffic_lights': traffic_lights_count,
        'signages': signages_count
    }
    return vid_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', message='No file part')
    
    file = request.files['file']
    
    if file.filename == '':
        return render_template('index.html', message='No selected file')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Perform object detection
        objects_count = detect_objects(file_path)

        # Generate PDF report
        report_path = generate_pdf_report(objects_count)
        return render_template('result.html', filename=filename, report_path=report_path)

    else:
        return render_template('index.html', message='Invalid file format')

@app.route('/download_report/<filename>', methods=['GET'])
def download_report(filename):
    report_filename = f"{filename.split('.')[0]}_report.pdf"  # Adjust file extension if needed
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], report_filename)

    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return render_template('result.html', filename=filename, message='Report not found')


if __name__ == '__main__':
    app.run(debug=True)
