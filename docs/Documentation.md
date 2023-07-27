# Documentation

## DocumentReader Class

### Purpose

The `DocumentReader` class is responsible for reading a Word document (.docx file) and storing its content for further processing. It uses the `python-docx` library to read the document.

### Methods

#### `__init__(self, file_path)`

This is the constructor method for the `DocumentReader` class. It takes one argument:

- `file_path`: A string representing the path to the Word document to be read.

This method initializes the `file_path` attribute with the given argument and the `document` attribute with `None`.

#### `read_document(self)`

This method reads the Word document specified by the `file_path` attribute and stores its content in the `document` attribute. It uses the `Document` function from the `python-docx` library to read the document.

If there's an error reading the document (e.g., the file doesn't exist or it's not a valid Word document), this method catches the exception and prints an error message. In this case, the `document` attribute remains `None`.

### Limitations

The `DocumentReader` class has the following limitations:

- It only supports Word documents (.docx files). Other file formats are not supported.
- It does not check if the file exists before trying to read it. If the file does not exist, an error will occur.
- It does not check if the file is a valid Word document. If the file is not a valid Word document, an error will occur.
- It does not provide any mechanism for handling errors. If an error occurs, it simply prints an error message and continues execution.

### TODO

The following improvements could be made to the `DocumentReader` class:

- Add support for other document formats, such as .doc or .odt.
- Check if the file exists before trying to read it. If the file does not exist, raise a custom exception.
- Check if the file is a valid Word document before trying to read it. If the file is not a valid Word document, raise a custom exception.
- Provide a mechanism for handling errors, such as a callback function or an error event.

---

## DocumentParser Class

### Purpose

The `DocumentParser` class is responsible for parsing the content of a Word document read by the `DocumentReader` class. It parses different elements of the document, such as headings, paragraphs, lists, tables, and images, and stores them for further processing.

### Methods

#### `__init__(self, document)`

This is the constructor method for the `DocumentParser` class. It takes one argument:

- `document`: A `Document` object representing the content of the Word document to be parsed.

This method initializes the `document` attribute with the given argument and the `headings`, `paragraphs`, `lists`, `tables`, and `images` attributes with empty lists.

#### `parse_headings(self)`

This method parses the headings in the `document` attribute and stores them in the `headings` attribute. It considers any paragraph with the style 'Heading 1' as a heading.

#### `parse_paragraphs(self)`

This method parses the paragraphs in the `document` attribute and stores them in the `paragraphs` attribute. It considers any paragraph with the style 'Normal' as a paragraph.

#### `parse_lists(self)`

This method is a placeholder for parsing lists in the `document` attribute. The `python-docx` library does not support parsing of lists directly, so this method currently does nothing.

#### `parse_tables(self)`

This method parses the tables in the `document` attribute and stores them in the `tables` attribute. It considers any table as a table.

#### `parse_images(self)`

This method is a placeholder for parsing images in the `document` attribute. The `python-docx` library does not support parsing of images directly, so this method currently does nothing.

### Limitations

The `DocumentParser` class has the following limitations:

- It only supports headings and paragraphs. Lists, tables, and images are not supported.
- It considers any paragraph with the style 'Heading 1' as a heading and any paragraph with the style 'Normal' as a paragraph. Other styles are not considered.
- It does not provide any mechanism for handling errors. If an error occurs, it simply continues execution.

### TODO

The following improvements could be made to the `DocumentParser` class:

- Add support for lists, tables, and images.
- Consider other styles for headings and paragraphs.
- Provide a mechanism for handling errors, such as a callback function or an error event.

---

## MarkdownConverter Class

### Purpose

The `MarkdownConverter` class is responsible for converting the parsed content of a Word document into Markdown. It takes the parsed content from the `DocumentParser` class and converts different elements, such as headings, paragraphs, lists, tables, and images, into their Markdown equivalents.

### Methods

#### `__init__(self, parsed_document)`

This is the constructor method for the `MarkdownConverter` class. It takes one argument:

- `parsed_document`: A `DocumentParser` object representing the parsed content of the Word document to be converted.

This method initializes the `parsed_document` attribute with the given argument and the `markdown_content` attribute with an empty string.

#### `convert_headings(self)`

This method converts the headings in the `parsed_document` attribute into Markdown and appends them to the `markdown_content` attribute. It converts each heading into a level 1 heading in Markdown (i.e., `# Heading`).

#### `convert_paragraphs(self)`

This method converts the paragraphs in the `parsed_document` attribute into Markdown and appends them to the `markdown_content` attribute. It converts each paragraph into a paragraph in Markdown (i.e., `Paragraph`).

#### `convert_lists(self)`

This method is a placeholder for converting lists into Markdown. The actual implementation will depend on how you parsed lists in the `DocumentParser` class.

#### `convert_tables(self)`

This method is a placeholder for converting tables into Markdown. The actual implementation will depend on how you parsed tables in the `DocumentParser` class.

#### `convert_images(self)`

This method is a placeholder for converting image references into Markdown. The actual implementation will depend on how you parsed images in the `DocumentParser` class.

### Limitations

The `MarkdownConverter` class has the following limitations:

- It only supports headings and paragraphs. Lists, tables, and images are not supported.
- It does not provide any mechanism for handling errors. If an error occurs, it simply continues execution.

### TODO

The following improvements could be made to the `MarkdownConverter` class:

- Add support for lists, tables, and images.
- Provide a mechanism for handling errors, such as a callback function or an error event.

---

## MarkdownWriter Class

### Purpose

The `MarkdownWriter` class is responsible for writing the converted Markdown content to a file. It takes the Markdown content from the `MarkdownConverter` class and writes it to a specified file.

### Methods

#### `__init__(self, markdown_content, output_path)`

This is the constructor method for the `MarkdownWriter` class. It takes two arguments:

- `markdown_content`: A string representing the Markdown content to be written.
- `output_path`: A string representing the path to the output file.

This method initializes the `markdown_content` and `output_path` attributes with the given arguments.

#### `write_markdown(self)`

This method writes the `markdown_content` attribute to the file specified by the `output_path` attribute. It uses Python's built-in `open` function to open the file and `write` method to write the content.

If there's an error writing the file (e.g., the file cannot be opened or the disk is full), this method catches the exception and prints an error message.

### Limitations

The `MarkdownWriter` class has the following limitations:

- It does not check if the file can be opened before trying to write to it. If the file cannot be opened, an error will occur.
- It does not check if there's enough disk space before trying to write to the file. If the disk is full, an error will occur.
- It does not provide any mechanism for handling errors. If an error occurs, it simply prints an error message and continues execution.

### TODO

The following improvements could be made to the `MarkdownWriter` class:

- Check if the file can be opened before trying to write to it. If the file cannot be opened, raise a custom exception.
- Check if there's enough disk space before trying to write to the file. If the disk is full, raise a custom exception.
- Provide a mechanism for handling errors, such as a callback function or an error event.

---

This documentation provides a detailed description of the `MarkdownWriter` class, including its purpose, methods, limitations, and a TODO list for future development.
