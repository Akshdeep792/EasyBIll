# EasyBIll
Here's a brief overview of what the script does: 


Header Extraction:

Uses PaddleOCR to extract text from the header of the image.
Processes the text to extract information like patient name, address, date, mobile number, and invoice number.
Table Extraction:

Provides two methods for table extraction: extract_table1 and extract_table2.
extract_table1 uses KMeans clustering to identify columns in the table.
extract_table2 uses image processing techniques, including thresholding, contour detection, and OCR, to extract tables.
Footer Extraction:

Uses PaddleOCR to extract text from the footer of the image.
Processes the text to extract information and creates key-value pairs.
Main Function (extractcsv):

Reads an image file specified by the image_path parameter.
Retrieves the retailer ID from the image path.
Calls the header, table, and footer extraction functions.
Writes the extracted information to separate CSV files (final.csv, table.csv, and footer.csv).
Command Line Arguments (currently commented out):

Originally, it appears that the script was designed to take image path and switch (1 or 2) as command-line arguments. However, in the __main__ block, the extractcsv function is called without any arguments.
Note:

The script may have dependencies on specific packages and models such as PaddleOCR, OpenCV, and scikit-learn (for KMeans clustering). Ensure that these dependencies are installed before running the script.
If you have any specific questions or if there's something you'd like assistance with, feel free to ask!
