import PyPDF2
a=PyPDF2.PdfFileReader("Change this line with PDF NAME. PDF Name must be enclosed within single inverted commas and PDF must be placed in same Directory")
# print(a.getDocumentInfo())
# print(a.getNumPages())
# print(a.getPage(60))
str = ""
for i in range (1):
    str +=a.getPage(i).extractText()
with open("Instructions For Students.txt", "w", encoding='utf-8') as f:
    f.write(str)