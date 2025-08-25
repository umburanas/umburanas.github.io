import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import pandas as pd
import io


def pdf_to_csv(pdf_path, csv_path):
    # Abra o PDF
    pdf_document = fitz.open(pdf_path)

    # Iterar sobre cada página
    all_data = []
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()

        # Converter a página para uma imagem
        img = Image.open(io.BytesIO(pix.tobytes()))

        # Usar OCR para extrair texto da imagem
        ocr_result = pytesseract.image_to_string(img)

        # Processar o resultado do OCR
        rows = ocr_result.split("\n")
        table_data = [row.split() for row in rows if row.strip()]

        all_data.extend(table_data)

    # Converter a tabela para um DataFrame do pandas
    df = pd.DataFrame(all_data)

    # Salvar a tabela como CSV
    df.to_csv(csv_path, index=False)

    print(f"PDF processado e salvo como CSV.")


pdf_path = "apoio_lista_de_especies.pdf"
csv_path = "saida.csv"

# Chamar a função para converter PDF para CSV
pdf_to_csv(pdf_path, csv_path)


# from PyPDF2 import PdfReader


# def read_pdf_to_dict(pdf_path):
#     pdf_reader = PdfReader(pdf_path)
#     num_pages = len(pdf_reader.pages)
#     pdf_dict = {}

#     for page in range(num_pages):
#         page_obj = pdf_reader.pages[page]
#         pdf_dict[f"Page {page + 1}"] = page_obj.extract_text()

#     return pdf_dict


# out = read_pdf_to_dict("apoio_lista_de_especies.pdf")
# print(out)


# import PyPDF2

# # Open the PDF file
# pdf_file = open("apoio_lista_de_especies.pdf", "rb")
# pdf_reader = PyPDF2.PdfReader(pdf_file)

# # Extract text from the first page
# page = pdf_reader.pages[0]
# text = page.extract_text()

# # Split text into lines
# lines = text.split("\n")

# # Process lines into a table (you may need to adjust this part depending on the table structure)
# table = [line.split() for line in lines]

# # Print the table
# for row in table:
#     print(row)


# import pdfplumber
# import csv

# pdf_file = "apoio_lista_de_especies.pdf"
# # Abra o arquivo PDF
# with pdfplumber.open("apoio_lista_de_especies.pdf") as pdf:
#     # Selecione a primeira página (ou a página desejada)
#     page = pdf.pages[0]

#     # Extraia a tabela da página
#     table = page.extract_table()

#     # Salve a tabela como um arquivo CSV
#     with open("output_pdfplumber.csv", mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerows(table)

# import camelot

# # Extraia tabelas do arquivo PDF
# tables = camelot.read_pdf(pdf_file, pages="1")

# # Salve a primeira tabela como um arquivo CSV
# tables[0].to_csv("output_camelot.csv")
