from fastapi import FastAPI, UploadFile , HTTPException
from fastapi.responses import JSONResponse
import pytesseract
from PIL import Image
import io
import PyPDF2
import magic
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # Change to your frontend URL in production, e.g., ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
@app.get("/")
async def root():
    return JSONResponse(content={"message": "Welcome to the File Upload and Text Extract App!"})
@app.post("/process-file")
async def process_file(file: UploadFile):

   try:
       # Read file content
       print("Reading file content", flush=True)
       file_content = await file.read()

       # Detect file type using python-magic
       mime_type = magic.from_buffer(file_content, mime=True)
       print(f"Detected MIME type: {mime_type}", flush=True)

       # Validate file type
       if mime_type not in ["image/jpeg", "image/png", "application/pdf"]:
           raise HTTPException(
               status_code=400,
               detail="Unsupported file type. Only JPEG, PNG, and PDF are allowed.",
           )

       # Extract text based on file type
       print(f"Processing {mime_type}", flush=True)
       if mime_type in ["image/jpeg", "image/png"]:
            try:
               image = Image.open(io.BytesIO(file_content))
            except Exception as e:
               print(e, flush=True)
               raise HTTPException(
                   status_code=400, detail="Failed to open the image file."
               )
            try:
               extracted_text = pytesseract.image_to_string(image)
            except Exception as e:
               print(e, flush=True)
               raise HTTPException(

                   status_code=400, detail="Failed to process the image file."
               )
       else:  # PDF
           try:
               pdf_file = io.BytesIO(file_content)
               pdf_reader = PyPDF2.PdfReader(pdf_file)
               extracted_text = ""
               for page in pdf_reader.pages:
                   extracted_text += page.extract_text() + "\n"
           except Exception as e:
               print(e, flush=True)
               raise HTTPException(
                   status_code=400, detail="Failed to process the PDF file."
               )
       print("Extracted text", flush=True)
       # Return result
       return JSONResponse(
           content={
               "file_name": file.filename,
               "extracted_text": extracted_text,

           }
       )

   except Exception as e:
       print(e, flush=True)
       raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

