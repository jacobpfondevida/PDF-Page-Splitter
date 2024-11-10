import fitz  # PyMuPDF
import os

class PDFProcessor:
    def __init__(self, file_path, folder_path):
        print("PDFProcessor class initializing")

        # Check if the file exists
        if not os.path.isfile(file_path):
            print(f"Error: The file {file_path} does not exist.")
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        try:
            # Try opening the PDF file
            self.pdf_document = fitz.open(file_path)
        except Exception as e:
            print(f"Error opening PDF: {e}")
            raise RuntimeError(f"Failed to open PDF file: {file_path}")

        self.total_pages = self.pdf_document.page_count
        self.current_page = 0  # Start from the first page
        self.file_path = file_path
        self.folder_path = folder_path
        print(f"PDFProcessor class initialized with {self.total_pages} pages")

    def get_page_image(self, page_number):
        """Converts the specified page to an image for display purposes."""
        try:
            page = self.pdf_document.load_page(page_number)
            pix = page.get_pixmap()
            image = pix.tobytes("ppm")  # Image bytes in PPM format
            return image
        except Exception as e:
            print(f"Error getting page image for page {page_number}: {e}")
            return None

    def get_total_pages(self):
        return self.total_pages

    def next_page(self):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
        return self.current_page

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
        return self.current_page

    def get_page_text(self, page_number):
        """Extracts text from the given page."""
        try:
            page = self.pdf_document.load_page(page_number)
            return page.get_text()
        except Exception as e:
            print(f"Error extracting text from page {page_number}: {e}")
            return ""

    def save_page_as_pdf(self, page_number, output_file_name):
        print("pressed save")
        try:
            print("in try block")
            output_file_path = f"{self.folder_path}/{output_file_name}.pdf"
            page = self.pdf_document.load_page(page_number)
            pdf_writer = fitz.open()  # Create a new PDF writer object
            pdf_writer.insert_pdf(self.pdf_document, from_page=page_number, to_page=page_number)
            pdf_writer.save(output_file_path)
            print(f"Saved page {page_number} as PDF: {output_file_path}")
        except Exception as e:
            print(f"Error saving page as PDF: {e}")

