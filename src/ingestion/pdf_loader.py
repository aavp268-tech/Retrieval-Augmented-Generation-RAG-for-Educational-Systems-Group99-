import fitz  # PyMuPDF
import logging

logger = logging.getLogger(__name__)

def load_pdf(pdf_path):
    """
    Load a single PDF and extract text page by page.
    """

    try:
        logger.info(f"Loading PDF: {pdf_path}")

        pdf = fitz.open(pdf_path)

        documents = []

        for page_num in range(len(pdf)):
            page = pdf[page_num]
            text = page.get_text()

            documents.append({
                "page": page_num + 1,
                "content": text
            })

        logger.info(f"Successfully loaded {pdf_path}")
        logger.info(f"Pages loaded: {len(documents)}")

        return documents

    except Exception as e:
        logger.error(f"Error loading PDF {pdf_path}: {e}")
        return []


def load_multiple_pdfs(pdf_paths):
    """
    Load multiple PDFs.
    """

    all_documents = []

    for pdf_path in pdf_paths:
        docs = load_pdf(pdf_path)
        all_documents.extend(docs)

    logger.info(f"Total pages loaded: {len(all_documents)}")

    return all_documents


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    pdfs = ["sample.pdf"]

    docs = load_multiple_pdfs(pdfs)

    print("\nFirst page preview:\n")

    if docs:
        print(docs[0]["content"][:1000])
