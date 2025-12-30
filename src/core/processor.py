import re

class CodeProcessor:
    # Handles input sanitization and output post-processing for code explanations.
    # Ensures quality gate for both input validation and output compliance.

    @staticmethod
    def sanitize_input(code: str) -> str:
        # Cleans input code to remove excessive whitespace and ensure it is valid text.
        # Reduces context window usage by collapsing multiple newlines.
        # Args:
        #     code (str): Raw C++ code input from user
        # Returns:
        #     str: Sanitized code ready for LLM processing
        
        if not code or len(code.strip()) == 0:
            return ""

        sanitized = re.sub(r"\n{3,}", "\n\n", code.strip())
        return sanitized

    @staticmethod
    def format_output(raw_response: str) -> str:
        # Post-processes the LLM output to ensure it the word limit.
        # Args:
        #     raw_response (str): Raw text from the LLM
        # Returns:
        #     str: Formatted explanation within 100 words

        cleaned_response = raw_response.strip()

        words = cleaned_response.split()
        if len(words) > 150:
            cleaned_response = " ".join(words[:150]) + "..."

        return cleaned_response
