# Video Analysis Web Application

## Introduction

This repository contains a web application developed for analyzing dashcam videos. The application allows users to upload a 1-minute video from a dashcam and performs object detection and counting of various elements such as potholes, road furniture, traffic lights, and signages. Additionally, it provides a dashboard display of the analysis results and enables users to download a detailed report in PDF format.

## Features

- Object detection and counting
- Dashboard display
- PDF report generation
- Bonus feature: Signage health analysis

## Technology Stack

- Backend Framework: Flask
- Video Processing and Object Detection: OpenCV
- PDF Generation: ReportLab
- Frontend Styling: HTML, CSS, Bootstrap

## Application Structure

1. **app.py**: Backend code written in Flask.
2. **index.html**: HTML template for the upload form.
3. **result.html**: HTML template for displaying analysis results.
4. **styles.css**: CSS stylesheet for styling the frontend.
5. **requirements.txt**: File containing Python dependencies.

## Workflow

1. **Video Upload**: Users upload a 1-minute dashcam video through the web interface.
2. **Object Detection and Counting**: The uploaded video is processed using OpenCV to detect and count various elements.
3. **Dashboard Display**: The analysis results are displayed on the web application dashboard.
4. **PDF Report Generation**: A detailed report summarizing the analysis results is generated in PDF format.
5. **Bonus Feature**: Signage health analysis using image processing techniques.

## Installation and Deployment

1. Clone the repository from GitHub.
2. Install required dependencies: `pip install -r requirements.txt`.
3. Run the Flask application: `python app.py`.
4. Access the web application in a browser using the provided URL.

## Conclusion

The video analysis web application provides a user-friendly interface for analyzing dashcam videos and extracting valuable insights. With its object detection, dashboard visualization, and PDF report generation features, it serves as a powerful tool for transportation management, road maintenance, and safety monitoring.

## Contact Information

For inquiries or feedback, please contact:
- [Developer Name]
- [Developer Email Address]
- [Developer GitHub Profile]
