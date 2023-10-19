# CSDF-Mini-Project

A spam filter using Transformer.

Fine tuned ALBERT transformer model.

Model: <a href="https://huggingface.co/NotShrirang/albert-spam-filter">https://huggingface.co/NotShrirang/albert-spam-filter</a><br>
Dataset: <a href="https://huggingface.co/datasets/NotShrirang/email-spam-filter">https://huggingface.co/datasets/NotShrirang/email-spam-filter</a>

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

Or

### Clone Repo:

```sh
git clone https://github.com/NotShrirang/Spam-Filter-using-ALBERT.git
```

```sh
cd Spam-Filter-using-ALBERT
```

### Install requirements:

```sh
pip install -r requirements.txt
```

### Run Streamlit Web App:

```sh
streamlit run app.py
```
