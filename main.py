from summarizer import read_txt, read_docx, read_pdf, read_html, generate_summary

def main():
    print("==== SMART TEXT SUMMARIZER ====\n")

    # Take file path from user
    file_path = input("Enter file path: ").strip()

    # Detect file type and read
    try:
        if file_path.endswith(".txt"):
            text = read_txt(file_path)

        elif file_path.endswith(".docx"):
            text = read_docx(file_path)

        elif file_path.endswith(".pdf"):
            text = read_pdf(file_path)

        elif file_path.endswith(".html"):
            text = read_html(file_path)

        else:
            print("❌ Unsupported file format.")
            return
    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
        return

    # Generate summary
    summary = generate_summary(text)

    print("\n==== SUMMARY ====\n")
    print(summary)

if _name_ == "_main_":
    main()