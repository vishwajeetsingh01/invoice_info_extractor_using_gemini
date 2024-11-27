# Invoice Info Extractor Using Gemini
 
# MultiModel - RAG

## Table of Contents

1. [Introduction](#introduction)
2. [Architecture](#architecture)
3. [Modules](#modules)
    - [PdfHandler](#pdfhandler)
    - [LlamaHandler](#llamahandler)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Running the Application](#running-the-application)
7. [Evaluations](#evaluations)

## Introduction

This project is designed to extract and process data from PDF files, including both tet and tables. The processed data is stored in vector databases, allowing for efficient retrival and
multi-model question-answering using large langauage models (LLMs).

## Architecture

The architecture of the project consists os three main engines:

### Persistence Engine

1. **PDF Files**: The processstarts with the input PDF files.
2. **PDF to Images**: Each page of the PDF is converted into an image.
3. **Table Transformer**: Tables are detected using the all-npnet model, creating a representtion of the textual data.
4. **all-mpnet Model**: Images are embedded using the CLIP model, creating a representation of the visual data.
6. **Text Store & Image Store**: The embeddings are stored in respective vector databases for tet and images.

### Retrival Engine

1. **Query**: The user provides a query.
2. **all-mpnet Model**: The query is embedded using the all-mpnet model.
3. **Vector Search (Text)**: A search is conducted in the text store to retrieve the top K relevant text embeddings.
4. **CLIP Model**: The query is also embedded using the CLIP model.
5. **Vector Search (Image)**: A search is conducted in the image store to retrieve the top K relevant image embeddings.

### Answer Engine

1. **Prompt Formation**: The retrieved text and image data are combined to form a prompt.
2. **LLaVA Multi-Model LLM**: The prompt is processed using the LLaVA Multi-Model LLM to generate an answer.
3. **Answer** The final answer is returned to the user.

![Architecture](data/readme_images/MultiModelRAG.jpeg)

## Project Structure
```
app.py
data
    images
    index
    pdf
    readme_images
    table_images
src
    config
        config.py
    llama_handler
        llama_handler.py
    pdf_handler
        pdf_handler.pdf
    prompts
        prompts.py
    utils
        table_transformer.py
        utils.py
    static
        styles.css
    templates
        index.html
    evaluations
        test_cases.csv
        evaluation_results.csv
        evaluation_results_only_image.csv
        evaluation_results_only_text.csv
        generate_results.py
        rages_evaluate.py
        results.csv
        results_only_image.csv
        results_only_text.csv
    requirements.tt
    README.md
```

## Modules

### PdfHandler

The `PdfHandler` class is responsible for processing PDF files. It performs the following tasks:
- Lists all PDF files in the specified directory.
- Converts each page of the PDFs into images.
- Extracts tables from these images using the table transformer model.
- Deletes existing processed folders before starting new processing.

### LlamaHandler

The `LlamaHandler` class handles the embeddings and retrieval of data, as well as generating answers using LLMs. It performs the following tasks:
- Embeds text and images using pre-trained models.
- Stores embeddings in vector databases.
- Retrieves relevant data based on a query.
- Generates context for the answer engine.
- Uses LLaVA Multi-Model LLM to provide answers.

## Installation

### Dependencies

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

### Ollama Setup

Download Ollama from here [Ollama](https://ollama.com/)

Run the following code after installing Ollama

```bash
ollama run llava
```


## Usage

### Running the Application

To start the Flask application, run:

```bash
python app.py
```

Navigate to https://localhost:5000 in your browser to access the application.

### Processing PDFs

Add Pdf files at this location ./data/pdf

To process the PDFs and persist the data, send a POST request to the `/persist` endpoint:

```bash
curl -X POST http://localhost:5000/persist
```

### Asking Questions

To ask question and receive an answer, send a POST request to the /answer endpoint with the question in the request body

```bash
curl -X POST -H "Content-Type: application/json" -d `{"question": "GIVE ME SUMMARY"}` http://localhost:5000/answer
```

### UI

This how the interactive UI looks

![UI](data/readme_images/UI.png)

## Evaluations

* Tested on [3 samples](evaluations/test_cases.csv)

### RAGAS

RAGAS (Retrieval-Augmented Generation Answer Scorer) is a Framework used to evaluate the quality of answers generated by large language models (LLMs) in a multi-model retrieval-augmented
generation (RAG) system. In a RAG setup, the LLM retrieves relevant information from a knowledge base (e.g., vector databases, documents) to generate and contectually relevant
responses. RAGAS focuses on scoring thses generated answers to ensure they meet specific quality criteria.

### Evaluation Results with Both Text and Image as Context

The evaluation results when using both text and image as context asre as follows:

| Metric                | Value    |
|-----------------------|----------|
| Faithfulness          | 0.333333 |
