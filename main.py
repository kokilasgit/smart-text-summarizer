from summarizer import read_txt, read_docx, read_pdf, read_html, generate_summary

def main():
    file_path = input("Enter file path: ")

    if file_path.endswith(".txt"):
        text = read_txt(file_path)

    elif file_path.endswith(".docx"):
        text = read_docx(file_path)

    elif file_path.endswith(".pdf"):
        text = read_pdf(file_path)

    elif file_path.endswith(".html") or file_path.endswith(".htm"):
        text = read_html(file_path)

    else:
        print("Unsupported file format!")
        return

    # Generate summary
    try:
        summary = generate_summary(text)
        print("\n----- SUMMARY -----\n")
        print(summary)
    except:
        print("Error: Text is too small to summarize.")

if __name__ == "__main__":
    main()
