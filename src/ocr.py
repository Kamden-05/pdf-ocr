import pytesseract
from tqdm import tqdm
from PIL import Image
from PyPDF2 import PdfWriter, PdfReader
import tempfile
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError,
)
import time
import io
from multiprocessing import Pool

def convert_to_pdf(image):
    return pytesseract.image_to_pdf_or_hocr(image, extension="pdf")


if __name__ == '__main__':

    file_path = r"C:\Users\Kamden\Developer\pdf-ocr\pdfs\test.pdf"
    images = convert_from_path(file_path)

    print("Converting images to pdfs...")
    start = time.time()
    with Pool() as pool:
        pages = pool.map(convert_to_pdf, images)
    end = time.time()
    print(f"Converted in {end - start} seconds\n")

    print("Creating searchable PDF...")
    merger = PdfWriter()
    for page in pages:
        merger.append(PdfReader(io.BytesIO(page)))

    merger.write("output.pdf")
    merger.close()
    print('done')
