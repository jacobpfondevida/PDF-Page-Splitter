from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QPushButton, QStackedWidget, QGraphicsView, QGraphicsScene, QWidget, QLineEdit, QMessageBox, QDialog, QComboBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QByteArray, Qt
import sys
import os
from pdf_processor import PDFProcessor

def get_ui_path(ui_filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ui_filename)
    return ui_filename

# PDF Processing Page
class PDFProcessingPage(QDialog):
    def __init__(self):
        print("PDFProcessingPage initializing")
        super().__init__()
        uic.loadUi(get_ui_path("pdfProcessingWidget.ui"), self)
        self.setWindowTitle("PDF Processing")

        # Graphics view to display the page
        self.graphicsView = self.findChild(QGraphicsView, "graphicsView")
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        # QLabel for the page name/label
        self.pageNameLabel = self.findChild(QLabel, "pageNameLabel")

        # Buttons to navigate through pages
        self.prevPageButton = self.findChild(QPushButton, "prevPageButton")
        self.nextPageButton = self.findChild(QPushButton, "nextPageButton")
        self.saveButton = self.findChild(QPushButton, "saveButton")
        self.saveAllPagesButton = self.findChild(QPushButton, "saveAllPagesButton")
        self.clearAllButton = self.findChild(QPushButton, "clearAllButton")

        self.fileNameLineEdit = self.findChild(QLineEdit, "fileNameLineEdit")
        self.fileNameLineEdit.editingFinished.connect(self.save_file_name)

        self.currentPageLabel = self.findChild(QLabel, "currentPageLabel")
        self.currentPageLineEdit = self.findChild(QLineEdit, "currentPageLineEdit")
        self.currentPageLineEdit.editingFinished.connect(self.jump_to_page)

        self.totalPagesLabel = self.findChild(QLabel, "totalPagesLabel")

        self.docTypeDropdownBox = self.findChild(QComboBox, "docTypeDropdownBox")
        self.docTypeDropdownBox.activated.connect(self.save_doc_type)

        # Connect button signals to methods
        self.prevPageButton.clicked.connect(self.show_prev_page)
        self.nextPageButton.clicked.connect(self.show_next_page)
        self.saveButton.clicked.connect(self.save_current_page)
        self.saveAllPagesButton.clicked.connect(self.save_all_pages)
        self.clearAllButton.clicked.connect(self.clear_page_configurations)

        # Initialize variables
        self.processor = None
        self.current_page = 0  # Initialize current_page
        self.total_pages = 0

        print("PDFProcessingPage initialized")

    def keyPressEvent(self, event):
        """Override to prevent Enter key from triggering button actions."""
        # If the Enter key is pressed and the focus is on the QLineEdit
        if event.key() == Qt.Key.Key_Return:
            event.accept()

    def set_paths(self, file_path, folder_path):
        """Set the file and folder paths passed from the main window."""
        self.file_path = file_path
        self.folder_path = folder_path

        self.processor = PDFProcessor(self.file_path, self.folder_path)  # Initialize PDFProcessor with the file path
        self.total_pages = self.processor.get_total_pages()
        self.page_configurations = [{"file_name" : "Enter file name", "doc_type": "Choose file type"} for page in range(self.total_pages)]
        self.update_page_display()  # Display the first page

    def show_page(self, pixmap):
        """Display PDF page in the QGraphicsView."""
        self.scene.clear()
        self.scene.addPixmap(pixmap)

    def set_page_name(self, name):
        """Set the page name (label) for the page."""
        self.pageNameLabel.setText(name)

    def show_prev_page(self):
        """Show the previous page."""
        if self.processor:
            self.page_configurations[self.current_page]['file_name'] = self.fileNameLineEdit.text().strip()
            self.page_configurations[self.current_page]['doc_type'] = self.docTypeDropdownBox.currentText()
            self.current_page = self.processor.prev_page()
            self.update_page_display()

    def show_next_page(self):
        """Show the next page."""
        if self.processor:
            self.page_configurations[self.current_page]['file_name'] = self.fileNameLineEdit.text().strip()
            self.page_configurations[self.current_page]['doc_type'] = self.docTypeDropdownBox.currentText()
            self.current_page = self.processor.next_page()
            self.update_page_display()

    def jump_to_page(self):
        """Jump to the page specified by the user."""
        # Get the page number from the input field (1-based input)
        print(f"Entered number: {self.currentPageLineEdit.text().strip()}")
        page_number = int(self.currentPageLineEdit.text()) - 1  # Convert to 0-based index
        print(f"Converted page number (0-based): {page_number}")

        # If the page number is invalid, it will jump to the closest valid page
        if self.processor:
            # Adjust for the 0-based index within the valid page range
            self.processor.go_to_page(page_number)
            self.current_page = self.processor.current_page
            print("updating from jump")
            self.update_page_display()  # Update the display after the page change

    def save_file_name(self):
        self.page_configurations[self.current_page]['file_name'] = self.fileNameLineEdit.text().strip()

    def save_doc_type(self):
        self.page_configurations[self.current_page]['doc_type'] = self.docTypeDropdownBox.currentText()

    def update_page_display(self):
        """Update the displayed page."""
        import traceback
        print(f"Called by: {''.join(traceback.format_stack())}")

        image_data = self.processor.get_page_image(self.current_page)
        pixmap = self.convert_to_pixmap(image_data)
        self.show_page(pixmap)

        self.currentPageLabel.setText("Current Page:")

        if self.totalPagesLabel.text() == "" and self.total_pages != 0:
            self.totalPagesLabel.setText(f"/ {self.total_pages}")

        if self.currentPageLineEdit:
            self.currentPageLineEdit.setText(f"{self.current_page+1}")

        if self.fileNameLineEdit:
            self.fileNameLineEdit.setText(self.page_configurations[self.current_page]['file_name'])
        if self.docTypeDropdownBox:
            self.docTypeDropdownBox.setCurrentText(self.page_configurations[self.current_page]['doc_type'])

    def convert_to_pixmap(self, image_data):
        """Convert the image bytes to a QPixmap."""
        byte_array = QByteArray(image_data)
        pixmap = QPixmap()
        pixmap.loadFromData(byte_array)
        return pixmap

    def save_current_page(self):
        """Save the current page to the output folder with the user-defined filename."""

        self.page_configurations[self.current_page]['file_name'] = self.fileNameLineEdit.text().strip()
        self.page_configurations[self.current_page]['doc_type'] = self.docTypeDropdownBox.currentText()

        if self.processor:
            file_name = self.page_configurations[self.current_page]['file_name']
            doc_type = self.page_configurations[self.current_page]['doc_type']

            if file_name and file_name != "Enter file name":
                # Get the output file path
                try:
                    self.processor.save_page_as_pdf(self.current_page, file_name, doc_type)
                except Exception as e:
                    warning_message = f"Error saving page {self.current_page + 1} as '{file_name}.pdf' in {doc_type} folder: {e}."
                    QMessageBox.warning(self, "Problem saving page", warning_message)

                success_message = f"Successfully saved page {self.current_page + 1} as '{file_name}.pdf' in {doc_type} folder."
                QMessageBox.about(self, "Success", success_message)

            else:
                # If no file name is provided, show an error
                QMessageBox.warning(self, "Invalid Filename", "Please enter a valid filename.")

    def save_all_pages(self):
        """Save all pages to their respective folders if all pages' information was entered.
           Otherwise, create a warning"""
        self.page_configurations[self.current_page]['file_name'] = self.fileNameLineEdit.text().strip()
        self.page_configurations[self.current_page]['doc_type'] = self.docTypeDropdownBox.currentText()

        file_name_indices = [i for i, d in enumerate(self.page_configurations) if d.get("file_name") == "Enter file name"]
        doc_type_indices = [i for i, d in enumerate(self.page_configurations) if d.get("doc_type") == "Choose file type"]

        if not file_name_indices and not doc_type_indices:
            try:
                if self.processor:
                    for i in range(len(self.page_configurations)):
                        current_file_name = self.page_configurations[i]['file_name']
                        current_doc_type = self.page_configurations[i]['doc_type']

                        self.processor.save_page_as_pdf(i, current_file_name, current_doc_type)

                    success_message = f"Successfully saved {self.total_pages} pages."
                    QMessageBox.about(self, "Success", success_message)
            except Exception as e:
                error_message = f"Error saving page named '{current_file_name}.pdf' in the {current_doc_type} folder: {e}"
                QMessageBox.warning(self, "Error saving pages", error_message)
        else:
            file_name_warning_message = ""
            doc_type_warning_message = ""
            warning_message = ""

            if file_name_indices:
                adjusted_file_name_page_numbers = [x + 1 for x in file_name_indices]
                file_name_warning_message = f"The following pages have no file name entered: {adjusted_file_name_page_numbers}."

            if doc_type_indices:
                adjusted_doc_type_page_numbers = [x + 1 for x in doc_type_indices]
                doc_type_warning_message = f"The following pages have no document type entered: {adjusted_doc_type_page_numbers}."

            warning_message = file_name_warning_message + "\n" + doc_type_warning_message

            QMessageBox.warning(self, "File(s) not configured", warning_message)

    def clear_page_configurations(self):
        self.page_configurations = [{"file_name" : "Enter file name", "doc_type": "Choose file type"} for page in range(self.total_pages)]
        self.update_page_display()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the .ui file
        uic.loadUi(get_ui_path('mainwindow.ui'), self)

        # Access buttons and other widgets from the UI
        self.inputFileButton = self.findChild(QPushButton, 'inputFileButton')
        self.outputFolderButton = self.findChild(QPushButton, 'outputFolderButton')
        self.proceedToProcessButton = self.findChild(QPushButton, 'proceedToProcessButton')

        # Connect buttons to their respective slots
        self.inputFileButton.clicked.connect(self.open_file_dialog)
        self.outputFolderButton.clicked.connect(self.open_output_folder_dialog)
        self.proceedToProcessButton.clicked.connect(self.show_pdf_processing_page)

        self.file_path = None
        self.folder_path = None

        # Create the PDF processing page
        self.pdf_page = PDFProcessingPage()

    def open_file_dialog(self):
        # Open a file dialog and get the selected file path
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")

        # Check if a file was selected
        if file_path:
            self.file_path = file_path  # Store the file path
            inputLabel = self.findChild(QLabel, "inputFileLabel")
            inputLabel.setText(f"Selected File: {file_path}")

    def open_output_folder_dialog(self):
        # Open a folder dialog to select an output folder
        folder_path = QFileDialog.getExistingDirectory(self, "Select Output Folder", "")

        if folder_path:
            self.folder_path = folder_path  # Store the folder path
            output_label = self.findChild(QLabel, 'outputFolderLabel')
            output_label.setText(f"Output Folder: {folder_path}")

    def show_pdf_processing_page(self):
        # Check if the paths are set before proceeding
        if self.file_path and self.folder_path:
            # Pass the paths to the PDFProcessingPage
            self.pdf_page.set_paths(self.file_path, self.folder_path)  # Ensure this method is called
            self.pdf_page.show()
            #self.stacked_widget.setCurrentWidget(self.pdf_page)
        else:
            QMessageBox.warning(self, "Missing Information", "Please select both a PDF file and an output folder.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
