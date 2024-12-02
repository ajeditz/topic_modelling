import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from pdf2image import convert_from_bytes

# If necessary, specify the path to the Tesseract executable (for Windows)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from analyser import paperAnalyser
def pdf_to_text(pdf_path):
    # Convert PDF to a list of images
    images = convert_from_path(pdf_path)
    
    text = ""
    for image in images:
        # OCR on each image
        text += pytesseract.image_to_string(image)
    
    return text


def uploaded_pdf_to_text(uploaded_pdf):
    # Read the uploaded file as bytes
    pdf_bytes = uploaded_pdf.read()

    # Convert the PDF bytes to a list of images
    images = convert_from_bytes(pdf_bytes)
    
    text = ""
    for image in images:
        # OCR on each image
        text += pytesseract.image_to_string(image)
    
    return text

# Example usage
pdf_path = '2.pdf'
pyqs= pdf_to_text(pdf_path)
# additional_instructions="Also give 3 most important questions"
# syllabus=pdf_to_text("ETR3C2DigitalElecronics.pdf")
# print(paperAnalyser(syllabus,pyqs,additional_instructions))
print(pyqs)