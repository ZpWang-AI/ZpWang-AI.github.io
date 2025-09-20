import os
from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path
from PIL import Image
from pathlib import Path as path


def concatenate_pdf(pdf_paths, output_pdf_path):
    pdf_writer = PdfWriter()

    for pdf_path in pdf_paths:
        pdf_reader = PdfReader(pdf_path)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(output_pdf_path, 'wb') as out_pdf:
        pdf_writer.write(out_pdf)

def pdf_to_png(pdf_path, ):
    print(pdf_path)
    images = convert_from_path(
        pdf_path, poppler_path=r'D:\NewDownload\Release-24.08.0-0\poppler-24.08.0\Library\bin',
    )
    max_width = max(img.width for img in images)
    img_list = []
    for p in range(len(images)):
        if p:
            black_line = Image.new('RGB', (images[0].width, 10), color='black')
            img_list.append(black_line)
        img_list.append(images[p])
    
    total_height = sum(img.height for img in img_list)
    
    # Create a new blank image with the combined dimensions
    combined_image = Image.new('RGB', (max_width, total_height))
    
    # Paste each image into the combined image
    current_height = 0
    for img in img_list:
        combined_image.paste(img, (0, current_height))
        current_height += img.height
    
    combined_image.save(path(pdf_path).parent/(path(pdf_path).stem+'.png'))

def main():
    # pdf_files = ['D:\ZpWang\Projects\01.02-AcademicPages\ZpWang-AI.github.io\files\Academic_CV_zp.pdf']  # Replace with your PDF file names
    # output_pdf = 'D:\ZpWang\Projects\01.02-AcademicPages\ZpWang-AI.github.io\files\Academic_CV_zp_.pdf'
    # output_folder = 'output_images'

    # # Create output folder if it doesn't exist
    # os.makedirs(output_folder, exist_ok=True)

    # # Concatenate PDFs
    # concatenate_pdf(pdf_files, output_pdf)
    # print(f'Combined PDF saved as: {output_pdf}')

    # Convert to PNG
    # pdf_to_png(r'D:\ZpWang\Projects\01.02-AcademicPages\ZpWang-AI.github.io\files\Academic_CV_zp.pdf', r'D:\ZpWang\Projects\01.02-AcademicPages\ZpWang-AI.github.io\files')
    pdf_to_png(r'D:\ZpWang\Projects\01.02-AcademicPages\ZpWang-AI.github.io\files\zpwang_resume_2025.pdf')
    # pdf_to_png(r'Academic_CV_zp.pdf', r'D:\ZpWang\Projects\01.02-AcademicPages\ZpWang-AI.github.io\files')
 
if __name__ == '__main__':
    main()