"""main.py

_summary_

_extended_summary_
"""

# Import the necessary classes from their respective modules
from docx import Document
from doc_rdr import DocumentReader
from doc_parser import DocumentParser
from md_converter import MarkdownConverter
from md_writer import MarkdownWriter

def main(input_path, output_path):
    """
    main _summary_

    _extended_summary_

    Args:
        input_path (_type_): _description_
        output_path (_type_): _description_
    """


    document = Document('your_document.docx')
    for style in document.styles:
        print(style.name)


    # Create a DocumentReader object and read the document
    doc_reader = DocumentReader(input_path)
    doc_reader.read_document()

    # Create a DocumentParser object and parse the document
    doc_parser = DocumentParser(doc_reader.document)
    doc_parser.parse_headings()
    doc_parser.parse_paragraphs()
    # Call the other parsing methods as needed

    # Create a MarkdownConverter object and convert the parsed content to Markdown
    md_converter = MarkdownConverter(doc_parser)
    md_converter.convert_headings()
    md_converter.convert_paragraphs()
    # Call the other conversion methods as needed

    # Create a MarkdownWriter object and write the Markdown content to a file
    md_writer = MarkdownWriter(md_converter.markdown_content, output_path)
    md_writer.write_markdown()

if __name__ == '__main__':
    # Specify the path to the input Word document and the output Markdown file
    INP = 'path_to_your_input_file.docx'
    OUTP = 'path_to_your_output_file.md'
    main(INP, OUTP)
