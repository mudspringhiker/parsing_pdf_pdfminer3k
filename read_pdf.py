
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
import re


def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content


def main(pdf='sdge_bill.pdf'):
    with open(pdf, "rb") as f:
        output = readPDF(f)
    meternumberregex = re.compile(r'(Meter Number: )\d{8}')
    meternumber = meternumberregex.search(output).group()
    print(meternumber)

    taxesfeesregex = re.compile(r'(Total Taxes & Fees on Electric Charges  -)\s+\$\d\.\d+')
    taxesfees = taxesfeesregex.search(output).group()
    print(taxesfees)


if __name__ == '__main__':
    main()

