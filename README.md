# Spam Filter using ALBERT

This project aims to build a spam filter using a fine-tuned ALBERT (A Lite BERT) Transformer model. The ALBERT model, pre-trained on a large corpus of text, is fine-tuned on a spam detection dataset to create an efficient and accurate spam filter.

## Table of Contents
- [Overview](#overview)
- [Usage](#usage)
    - [Using the Classifier in Your Code](#to-use-this-classifier-in-your-code)
    - [Installation](#installation)
    - [Running the Streamlit Web App](#run-streamlit-web-app)
- [License](https://github.com/NotShrirang/Spam-Filter-using-ALBERT/blob/main/LICENSE)

## Overview
A transformers based deep learning for binary text classification. There are 2 classes "Spam" and "Not spam".
Model and dataset is deployed on HuggingFace.
- Model: <a href="https://huggingface.co/NotShrirang/albert-spam-filter">https://huggingface.co/NotShrirang/albert-spam-filter</a><br>
- Dataset: <a href="https://huggingface.co/datasets/NotShrirang/email-spam-filter">https://huggingface.co/datasets/NotShrirang/email-spam-filter</a>


## Usage
### To use this classifier in your code:
```py
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

tokenizer = AutoTokenizer.from_pretrained("NotShrirang/albert-spam-filter")
model = AutoModelForSequenceClassification.from_pretrained("NotShrirang/albert-spam-filter")

classifier = pipeline('text-classification',
                model=model,
                tokenizer=tokenizer
             )

prediction = classifier("<Your Text>")[0]
```
## Installation:
To run this project, you will need Python and Streamlit installed on your system. You can install the required packages using the provided `requirements.txt` file.
1. Clone Repo:

```sh
git clone https://github.com/NotShrirang/Spam-Filter-using-ALBERT.git
```
2. Change project directory:
```sh
cd Spam-Filter-using-ALBERT
```
3. Get requirements:
```sh
pip install -r requirements.txt
```

## Run Streamlit Web App:

```sh
streamlit run app.py
```
