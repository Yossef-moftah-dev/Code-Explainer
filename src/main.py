import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import gradio as gr
from core.processor import CodeProcessor
from llm.client import StarCoderClient
from llm.prompts import SYSTEM_PROMPT

# Initialize components
try:
    llm_client = StarCoderClient()
    processor = CodeProcessor()
except ValueError as e:
    print(f"Configuration Error: {e}")
    print("Please ensure .env file is properly configured with API_TOKEN")
    sys.exit(1)


def explain_code_pipeline(code_input):
    # Orchestrates the flow: Input -> Sanitize -> Prompt -> Inference -> Format -> Output
    # Args:
    #     code_input (str): Raw C++ code from user
    # Returns:
    #     str: Beginner-friendly explanation of the code

    # 1. Validation
    sanitized_code = processor.sanitize_input(code_input)
    if not sanitized_code:
        return "Please enter valid C++ code."

    # 2. Prompt Engineering
    full_prompt = SYSTEM_PROMPT.format(code_input=sanitized_code)

    # 3. Inference
    raw_explanation = llm_client.generate_explanation(full_prompt)

    # 4. Post-processing
    final_output = processor.format_output(raw_explanation)

    return final_output


# Gradio Interface Definition
with gr.Blocks(title="C++ CodeExplainer", theme=gr.themes.Soft()) as app:
    gr.Markdown("# C++ CodeExplainer")
    gr.Markdown(
        "Paste your C++ code below to get a **simple, beginner-friendly explanation**."
    )

    with gr.Row():
        with gr.Column():
            code_input = gr.Code(language="cpp", label="Input C++ Source Code", lines=10)
            explain_btn = gr.Button("Explain Code", variant="primary", size="lg")

        with gr.Column():
            explanation_output = gr.Textbox(
                label="AI Explanation", interactive=False, lines=8
            )

    # Event binding
    explain_btn.click(
        fn=explain_code_pipeline, inputs=code_input, outputs=explanation_output
    )


if __name__ == "__main__":
    print("Starting C++ CodeExplainer...")
    print("Open http://localhost:7860 in your browser")
    app.launch(server_name="0.0.0.0", server_port=7860, share=False)
