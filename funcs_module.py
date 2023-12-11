import fitz
import pandas as pd
import re

def extract_images_from_page(pdf_document, page, page_number):
    image_list = page.get_images(full=True)
    if image_list is None:
        return None
    else:
        images_name = []
        for img_index, img_info in enumerate(image_list):
            xref = img_info[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_filename = f"image_{page_number + 1}_{img_index + 1}.png"
            images_name.append(image_filename)
            with open(image_filename, "wb") as image_file:
                image_file.write(image_bytes)
        return images_name

def separate_header(text):
    header_pattern = r'^\d+\s.*\s\d+$'
    match = re.search(header_pattern, text, re.MULTILINE)
    
    if match:
        header = match.group(0)
        header_end_index = match.end()
        main_text = text[header_end_index:]
    else:
        header = ''
        main_text = text
    
    return header, main_text

def process_toc(pdf_document, toc):
    parts_list = []
    
    for i in range(len(toc)):
        title = toc[i][1]  
        start_page = toc[i][2]
        
        if i != len(toc) - 1:
            end_page = toc[i + 1][2]
        else:
            end_page = len(pdf_document)

        part_text = []
        part_images = []
        for j in range(start_page - 1, end_page):
            page = pdf_document.load_page(j)
            page_images = extract_images_from_page(pdf_document, page, j)
            
            if page_images is not None:
                part_images.append(page_images)
                
            text = page.get_text("text")
            page_header, page_text = separate_header(text)
            part_text.append(page_text)
            
        if i != len(toc) - 1:
            part_text[0] = part_text[0].split(title)[1]
            next_title = toc[i + 1][1]
            part_text[-1] = part_text[-1].split(next_title)[0]
        else:
            part_text[0] = part_text[0].split(title)[1]

        part_dict = {
            'title': title,
            'pages': f'{start_page}-{end_page}',
            'text': part_text,
            'images': part_images
        }

        parts_list.append(part_dict)

    pd.set_option('display.max_colwidth', 10000)
    toc_pd = pd.DataFrame(toc)
    list_pd = pd.DataFrame(parts_list)
    print(toc_pd)
    print(list_pd)

    return parts_list

def main(pdf_path):
    pdf_document = fitz.open(pdf_path)
    toc = pdf_document.get_toc(simple=True)
    parts_list = process_toc(pdf_document, toc)
    pdf_document.close()

    return parts_list