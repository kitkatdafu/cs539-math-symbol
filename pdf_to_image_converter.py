from pdf2image import convert_from_path
import sys
import os
import random

"""
    This module converts directory containing PDF files
    to images with 600 DPI and save them in given output directory
    Usage: python convert_pdf_to_image.py <PDF_files_dir> <output_img_dir>
"""


def create_images_from_pdfs(pdf_dir, output_dir, rand):
    '''
    Render each PDF file as image in 600 DPI
    :param pdf_dir: Directory with PDF files
    :param output_dir: Output directory for storing image files for each PDF file
    :return: None
    '''
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    pdf_files = []
    for _, _, fileList in os.walk(pdf_dir):
        pdf_files.extend(fileList)
        break
    total = 1
    for pdf_file in pdf_files:
        if pdf_file == '.DS_Store':
            continue
        pdf_name = pdf_file.split(".pdf")[0]
        output_path = os.path.join(output_dir, pdf_name)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        pages = convert_from_path(os.path.join(pdf_dir, pdf_file), 600, grayscale=False)
        index_range = range(len(pages))
        if rand:
            index_range = random.sample(index_range, 4)
        for i in index_range:
            pages[i].save(os.path.join(output_path, str(total) + ".png"), 'PNG')
            total += 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 convert_pdf_to_image.py <PDF_files_dir> <output_dir>")
        exit(0)
    pdf_dir = sys.argv[1]
    output_dir = sys.argv[2]
    if sys.argv[3] == 'False':
        rand = False
    else:
        rand = True
    create_images_from_pdfs(pdf_dir, output_dir, rand)
