import pdfplumber

pdf_path = 'EL_FELLAH_Meryem_Rapport_PrjFinal.pdf'
text = ''

with pdfplumber.open(pdf_path) as pdf:
    page_count = len(pdf.pages)
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + '\n\n'

with open('extracted_text.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print(f'Text extracted successfully. Total pages: {page_count}')
print(f'Text saved to: extracted_text.txt')
