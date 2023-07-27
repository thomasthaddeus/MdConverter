# Word to Markdown Converter

This project is a Python application that converts Word documents to Markdown files. It uses the `python-docx` library to read Word documents, parses the content into headings, paragraphs, lists, tables, and images, converts these elements to their Markdown equivalents, and writes the result to a Markdown file.

## Structure

```bash
├── docs
│   ├── Documentation.md
│   ├── DocumentParserClass.md
│   └── DocumentReaderClass.md
├── LICENSE
├── README.md
├── script.py
├── scripts
│   ├── init_repo.sh
│   └── make_repo.sh
├── src
│   ├── docx_ingest
│   │   ├── doc_parser.py
│   │   ├── doc_rdr.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── main.py
│   └── md_converter
│       ├── __init__.py
│       ├── md_converter.py
│       └── md_writer.py
└── tests
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-311.pyc
    │   └── test_main.cpython-311-pytest-7.4.0.pyc
    └── test_main.py
```

## Requirements

- Python 3.6 or later
- `python-docx` library

## Installation

1. Clone this repository to your local machine.
2. Install the required Python libraries with `pip install -r requirements.txt`.

## Usage

1. Run `python main.py --input input.docx --output output.md` to convert `input.docx` to `output.md`.
2. Check `output.md` for the result.

## Limitations

This is a basic implementation and may not work for all Word documents, especially those with complex formatting, lists, or images. The `python-docx` library does not support parsing of lists or images directly, so these features are not currently supported.

## Contributing

Contributions are welcome! Please submit a pull request or create an issue to discuss proposed changes.

---

This README provides a brief description of the project, lists the requirements, explains how to install and use the application, mentions the current limitations, and invites contributions.

Might want to add more details or sections, depending on the project specifications **TBD**.
