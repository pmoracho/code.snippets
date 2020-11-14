from pdfminer.layout import LAParams, LTTextBox, LTFigure, LTImage
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator

pdf_file ='/home/pmoracho/Descargas/handbook-of-marketing-scale-2011.pdf'

with open(pdf_file, 'rb') as fp:

    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = list(PDFPage.get_pages(fp))

    for page in pages[30:31]:
        interpreter.process_page(page)
        layout = device.get_result()

        for lobj in layout:

            if isinstance(lobj, LTTextBox):
                text = lobj.get_text()
                x, y, text = lobj.bbox[0], lobj.bbox[3], text
                # print("({0}, {1}) {2}".format(x, y, text))
                print(text)

