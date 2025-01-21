# File Text Extraction Service

A web application that extracts text from images and PDF files using OCR (Optical Character Recognition) technology and PDF parsing.

## Overview

This project consists of two main components:
1. A FastAPI backend service that processes files and extracts text
2. A simple, user-friendly HTML frontend interface for file uploads

## Features

- Support for multiple file formats:
  - Images (JPEG, PNG)
  - PDF documents
- Real-time text extraction
- Interactive web interface
- Loading indicator for processing feedback
- Error handling and user notifications
- Cross-Origin Resource Sharing (CORS) enabled

## Technology Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs with Python
- **Tesseract OCR**: (via `pytesseract`) for extracting text from images
- **PyPDF2**: For parsing and extracting text from PDF files
- **python-magic**: For file type detection
- **Pillow (PIL)**: For image processing

### Frontend
- **HTML5**
- **CSS3**: Custom styling with responsive design
- **JavaScript**: Vanilla JS for handling file uploads and API interactions

## Setup and Installation

1. Clone the repository:
bash
git clone https://github.com/Abhay075/Text-Extraction-from-Files

2. Install the required Python packages:
bash
pip install -r requirements.txt

3. Install Tesseract OCR on your system:
- For Ubuntu/Debian:
  ```bash
  sudo apt-get install tesseract-ocr
  ```
- For macOS:
  ```bash
  brew install tesseract
  ```
- For Windows:
  Download and install from the [official GitHub releases](https://github.com/UB-Mannheim/tesseract/wiki)

4. Run the FastAPI server:
bash
uvicorn main:app --reload


5. Open `index.html` in a web browser or serve it using a local server.

## Usage

1. Open the web interface in your browser
2. Click "Choose a file" to select an image or PDF
3. Click "Upload and Process" to extract text
4. View the extracted text in the output box below

## API Endpoints

### POST /process-file
- Accepts multipart form data with a file
- Supports image (JPEG, PNG) and PDF files
- Returns JSON with extracted text and filename

## Error Handling

The application includes comprehensive error handling for:
- Unsupported file types
- File processing failures
- Server errors
- Network issues

## Development

The project is structured for easy maintenance and extension:
- `main.py`: Contains the FastAPI backend logic
- `index.html`: Contains the frontend interface and JavaScript

## Deployment

The backend is currently deployed on Render.com. To deploy your own instance:

1. Create a new Web Service on Render
2. Connect your repository
3. Set the build command and start command
4. Update the API endpoint URL in `index.html`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your chosen license here]

## Acknowledgments

- Tesseract OCR for image text extraction
- FastAPI for the efficient backend framework
- PyPDF2 for PDF processing capabilities
