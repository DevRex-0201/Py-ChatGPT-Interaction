# Tkinter ChatGPT Interaction Project
## Project Overview

This project is a simple desktop application created with Tkinter that allows users to interact with OpenAI's ChatGPT. Users can input Markdown-formatted text, and the application sends the input to ChatGPT, displaying the generated response. Additionally, the application supports saving and loading conversations from files.

## Requirements

- Python 3.x
- Tkinter (included in most Python installations)
- OpenAI Python library (install using `pip install openai`)
- Pillow (for ScrolledText, install using `pip install Pillow`)

## Setup

1. **Install Dependencies:**
    ```bash
    pip install openai Pillow
    ```

2. **OpenAI API Key:**
    - Replace the placeholder API key in the script with your actual OpenAI API key.

## Running the Application

1. **Run the Script:**
    ```bash
    python script.py
    ```
    The application window will appear.

2. **Input Markdown Text:**
    - Enter Markdown-formatted text in the input area.

3. **Process Input:**
    - Click the "処理" (Process) button to send the input to ChatGPT.

4. **View Output:**
    - The generated response from ChatGPT will be displayed in the output area.

5. **Save/Load Conversations:**
    - Use the "ファイル" (File) menu to save or load conversations.

## Customization

- **Model Configuration:**
    - You can adjust the model name and parameters in the `process_input` function based on your ChatGPT version and preferences.

## Notes

- This project is a basic example of integrating Tkinter with OpenAI's ChatGPT. You can extend it to add more features or integrate with other applications.

- Ensure you have a stable internet connection for using the OpenAI API.

- The project assumes basic familiarity with Tkinter and OpenAI API usage.
