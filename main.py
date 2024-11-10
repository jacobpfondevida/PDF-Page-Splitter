from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QPushButton, QStackedWidget, QGraphicsView, QGraphicsScene, QWidget, QLineEdit, QMessageBox, QDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QByteArray
import sys
from pdf_processor import PDFProcessor  # Assuming you have this class defined correctly

# PDF Processing Page
class PDFProcessingPage(QDialog):
    def __init__(self):
        print("PDFProcessingPage initializing")
        super().__init__()
        uic.loadUi("pdfProcessingWidget.ui", self)
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

        # QLineEdit for the user to input the filename
        self.fileNameLineEdit = self.findChild(QLineEdit, "fileNameLineEdit")

        self.currentPageLabel = self.findChild(QLabel, "currentPageLabel")

        # Connect button signals to methods
        self.prevPageButton.clicked.connect(self.show_prev_page)
        self.nextPageButton.clicked.connect(self.show_next_page)
        self.saveButton.clicked.connect(self.save_current_page)

        # Initialize variables
        self.processor = None
        self.current_page = 0  # Initialize current_page

        print("PDFProcessingPage initialized")

    def set_paths(self, file_path, folder_path):
        """Set the file and folder paths passed from the main window."""
        self.file_path = file_path
        self.folder_path = folder_path
        self.processor = PDFProcessor(self.file_path, self.folder_path)  # Initialize PDFProcessor with the file path
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
            self.current_page = self.processor.prev_page()
            self.update_page_display()

    def show_next_page(self):
        """Show the next page."""
        if self.processor:
            self.current_page = self.processor.next_page()
            self.update_page_display()

    def update_page_display(self):
        """Update the displayed page."""
        image_data = self.processor.get_page_image(self.current_page)
        pixmap = self.convert_to_pixmap(image_data)
        self.show_page(pixmap)
        self.currentPageLabel.setText(f"Current Page: {self.current_page + 1} / {self.processor.get_total_pages()}")

    def convert_to_pixmap(self, image_data):
        """Convert the image bytes to a QPixmap."""
        byte_array = QByteArray(image_data)
        pixmap = QPixmap()
        pixmap.loadFromData(byte_array)
        return pixmap

    def save_current_page(self):
        """Save the current page to the output folder with the user-defined filename."""
        if self.processor:
            # Get the custom file name from the QLineEdit
            file_name = self.fileNameLineEdit.text().strip()
            print(f"stripped name: {file_name}")
            if file_name:
                # Get the output file path
                self.processor.save_page_as_pdf(self.current_page, file_name)
                print("post processor save")
            else:
                # If no file name is provided, show an error
                QMessageBox.warning(self, "Invalid Filename", "Please enter a valid filename.")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the .ui file
        uic.loadUi('mainwindow.ui', self)

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

        sender = self.sender()

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
