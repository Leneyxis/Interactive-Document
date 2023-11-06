# Interactive Document

This simple Python script is designed to extract and index information from PDF(resumes in this case) documents, and then query the indexed data using the OpenAI GPT-3 model.

```markdown

## Getting Started

### Prerequisites

1. Python: Make sure you have Python installed. This code is written in Python 3.

### Installation

1. Clone this repository or download the code.
2. Install the required Python packages using pip:

```bash
pip install openai dotenv llama_index
```

3. Create a `.env` file in the project directory and add your OpenAI API key in the following format:

```plaintext
key=YOUR_OPENAI_API_KEY
```

## Usage

1. Run the script `main.py`. This script does the following:

   a. Loads the environment variables, including your OpenAI API key, from the `.env` file.
   b. Downloads the PDFReader module and loads the PDF data from the specified PDF file.
   c. Creates an index of the loaded documents.
   d. Saves the index in a JSON file for reuse to save on API calls.
   e. Queries the index with a specified question to extract essential details.

2. You can modify the query in the script to retrieve different information from the indexed PDF documents.



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This code uses the OpenAI GPT-3 model to perform document indexing and querying.
- The `llama_index` library is used to simplify the PDF document loading and indexing process.
