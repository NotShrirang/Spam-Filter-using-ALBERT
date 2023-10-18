import streamlit as st

st.title("Spam Filter using ALBERT")

st.sidebar.title("About")
st.sidebar.info(
    "This is a demo of a spam filter using ALBERT. The model was trained on the [Email Spam Collection Dataset](https://huggingface.co/datasets/NotShrirang/email-spam-filter)."
)

st.subheader("Enter your email text below:")

text = st.text_area("Enter text here...", label_visibility="hidden")

predict_button = st.button("Check")
if predict_button:
    st.info("Predicting...")
    from classifier import load_model, create_pipeline, predict
    model, tokenizer = load_model()
    classifier = create_pipeline(model, tokenizer)
    prediction = predict(classifier, text[:512])
    st.subheader("Prediction: " + prediction['label'])
    st.subheader("Confidence: " + str(round(prediction['score'], 4)))
    st.success("Oof! That's a spam email!" if prediction['label'] == "Spam" else "Yay! That's not a spam email!")