from glob import glob
import PyPDF2
import os


def pdf_rotate(p_file, p_angle):
    basename = os.path.basename(p_file)
    file = PyPDF2.PdfFileReader(open(p_file, 'rb'))
    file_output = PyPDF2.PdfFileWriter()
    for page_num in range(file.numPages):
        page = file.getPage(page_num)
        page.rotateClockwise(p_angle)
        file_output.addPage(page)
    with open("ro_" + basename, 'wb') as f:
        file_output.write(f)


path = "C:\\Users\\novuf\\Downloads\\kimetsu\\*.pdf"

for f in glob(path):
    print(f)
    pdf_rotate(f, 90)
