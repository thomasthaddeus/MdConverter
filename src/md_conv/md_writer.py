"""
_summary_

_extended_summary_
"""

class MarkdownWriter:
    """
     _summary_

    _extended_summary_
    """
    def __init__(self, markdown_content, output_path):
        self.markdown_content = markdown_content
        self.output_path = output_path

    def write_markdown(self):
        """
        write_markdown _summary_

        _extended_summary_
        """
        try:
            with open(file=self.output_path, mode='w', encoding='utf-8') as fil:
                fil.write(self.markdown_content)
        except Exception as exc:
            print(f"Error writing markdown file: {exc}")
