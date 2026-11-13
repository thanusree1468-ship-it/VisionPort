
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import torch

# Page configuration
st.set_page_config(
    page_title="YOLO",
    page_icon="🚦",
    layout="wide"
)

# Application title
st.title("🚦 VisionPort v0.1")
st.write("GPU-Accelerated Traffic Object Detection")

# Check GPU availability
device = "cuda" if torch.cuda.is_available() else "cpu"

st.write(f"Running on: **{device.upper()}**")

# Load YOLO model
@st.cache_resource
def load_model():
    model = YOLO("yolov8n.pt")
    return model

model = load_model()

# Upload image
uploaded_file = st.file_uploader(
    "Upload a Traffic Image",
    type=["png", "jpg", "jpeg"]
)

# Object detection
if uploaded_file is not None:

    # Read uploaded image
    image = Image.open(uploaded_file).convert("RGB")

    # Run YOLO prediction
    with st.spinner("Detecting objects..."):
        results = model.predict(
            source=image,
            device=device
        )

    # Get detected image
    result_image = results[0].plot()

    # Display images side by side
    st.subheader("Traffic Image Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")

        st.image(
            image,
            caption="Uploaded Traffic Image",
            use_container_width=True
        )

    with col2:
        st.subheader("Detection Results")

        st.image(
            result_image,
            caption="YOLO Detected Image",
            channels="BGR",
            use_container_width=True
        )

    # Display detection summary
    st.subheader("Detection Summary")

    boxes = results[0].boxes

    if boxes is not None and len(boxes) > 0:

        class_counts = {}

        for box in boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]

            class_counts[class_name] = (
                class_counts.get(class_name, 0) + 1
            )

        st.write(f"**Total Objects Detected:** {len(boxes)}")

        # Display individual object counts
        cols = st.columns(min(len(class_counts), 4))

        for index, (name, count) in enumerate(class_counts.items()):
            with cols[index % len(cols)]:
                st.metric(name.capitalize(), count)

    else:
        st.warning("No objects detected in the uploaded image.")

else:
    st.info("Please upload a traffic image to start object detection.")
