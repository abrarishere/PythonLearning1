import re

class CodeEditorHighlighter:
    def __init__(self, parent=None):
        self.highlighting_rules = []

        # Python
        self.add_highlighting_rule(r'\bimport\b', {'color': '#FF8740', 'bold': True})
        self.add_highlighting_rule(r'\bdef\b', {'color': '#FF8740', 'bold': True})
        self.add_highlighting_rule(r'\bclass\b', {'color': '#FF8740', 'bold': True})

        # JavaScript
        self.add_highlighting_rule(r'\bfunction\b', {'color': '#C586C0', 'bold': True})

        # HTML
        self.add_highlighting_rule(r'<.*?>', {'color': '#00A2E8'})

        # CSS
        self.add_highlighting_rule(r'\{|\}', {'color': '#00A2E8'})
        self.add_highlighting_rule(r'\b\w+\b', {'color': '#00A2E8', 'italic': True})

    def add_highlighting_rule(self, pattern, style):
        rule = (re.compile(pattern), style)
        self.highlighting_rules.append(rule)

    def highlight_block(self, text):
        formatted_text = []

        for rule in self.highlighting_rules:
            pattern, style = rule
            for match in pattern.finditer(text):
                start, end = match.span()
                formatted_text.append((start, end, style))

        return formatted_text
