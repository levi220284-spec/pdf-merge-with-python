import PyPDF2

def merge_pdfs(pdf_list, output_filename):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        try:
            merger.append(pdf)
            print(f"Added {pdf}")
        except FileNotFoundError:
            print(f"File {pdf} not found, skipping...")
    merger.write(output_filename)
    merger.close()
    print(f"Merged PDF saved as {output_filename}")

def main():
    print("PDF Merger")
    pdf_files = input("Enter the PDF filenames to merge, separated by commas: ").split(",")
    pdf_files = [pdf.strip() for pdf in pdf_files]  # remove extra spaces
    output_file = input("Enter the output PDF filename (e.g., merged.pdf): ")
    merge_pdfs(pdf_files, output_file)

if __name__ == "__main__":
    main()

