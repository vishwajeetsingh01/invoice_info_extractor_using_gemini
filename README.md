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
multi-modal question-answering using large langauage modals (LLMs).

## Architecture

The architecture of the project consists os three main engines:

### Persistence Engine

1. **PDF Files**: The processstarts with the input PDF files.
2. **PDF to Images**: Each page of the PDF is converted into an image.
3. **Table Transformer**: Tables are detected using the all-npnet modal, creating a representtion of the textual data.
4. **all-mpnet Modal**: Images are embedded using the CLIP modal, creating a representation of the visual data.
6. **Text Store & Image Store**: The embeddings are stored in respective vector databases for tet and images.

### Retrival Engine

1. **Query**: The user provides a query.
2. **all-mpnet Modal**: The query is embedded using the all-mpnet modal.
3. **Vector Search (Text)**: A search is conducted in the text store to retrieve the top K relevant text embeddings.
4. **CLIP Modal**: The query is also embedded using the CLIP modal.
5. **Vector Search (Image)**: A search is conducted in the image store to retrieve the top K relevant image embeddings.

### Answer Engine

1. **Prompt Formation**: The retrieved text and image data are combined to form a prompt.
2. **LLaVA Multi-Modal LLM**: The prompt is processed using the LLaVA Multi-Modal LLM to generate an answer.
3. **Answer** The final answer is returned to the user.

![Architecture](data/readme_images/MultiModalRAG.jpeg)

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
- Uses LLaVA Multi-Modal LLM to provide answers.

## Installation

### Dependencies

