from funcs_module import main
import sys

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python parse_pdf.py <pdf_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    result = main(pdf_path)
