import streamlit as st
import sys
from pathlib import Path
from src.inference import InferenceYolo
from src.utils import save_metadata, load_metadata, get_unique_classes_and_counts

sys.path.append(str(Path(__file__).parent))


def init_session_state():
    session_defaults = {
        "metadata": None,
        "unique_classes_and_counts": {},
    }
    for key, value in session_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_session_state()

st.set_page_config(page_title="YOLOV11 Search Application")

st.title("Computer Vision Powered Search Application")
process_type = st.radio(
    "Choose an option:",
    ["Process new Images", "Load existing metadata"],
    horizontal=True,
)
with st.expander(process_type, expanded=True):

    if process_type == "Process new Images":
        col1, col2 = st.columns(2)
        with col1:
            directory_path = st.text_input(
                "images directory path", placeholder="path/to/images"
            )

        with col2:
            model_path = st.text_input("Model weights path", "yolo11m.pt")

        if st.button("Start Inference"):

            if directory_path and model_path:

                try:
                    with st.spinner("Running Object Detection..."):
                        inferencer = InferenceYolo(model_path)
                        metadata = inferencer.process_directory(directory_path)
                        saved_path = save_metadata(metadata, directory_path)
                        st.code(str(saved_path))
                        st.success(
                            f"Inference completed successfully! for {len(metadata)} Images and  Metadata saved at: {saved_path}"
                        )
                        st.session_state["metadata"] = metadata
                        unique_classes_and_counts = get_unique_classes_and_counts(
                            metadata
                        )
                        st.session_state["unique_classes_and_counts"] = (
                            unique_classes_and_counts
                        )
                except Exception as e:
                    st.error(f"Error occurred during inference: {str(e)}")
            else:
                st.warning(
                    "Please provide both the images directory path and the model weights path."
                )
    else:
        metadata_path = st.text_input(
            "Metadata file path", placeholder="path/to/metadata.json"
        )
        if st.button("Load Metadata"):
            if metadata_path:
                try:
                    with st.spinner("Loading metadata..."):
                        metadata = load_metadata(metadata_path)
                        st.session_state["metadata"] = metadata
                        unique_classes_and_counts = get_unique_classes_and_counts(
                            metadata
                        )
                        st.session_state["unique_classes_and_counts"] = (
                            unique_classes_and_counts
                        )

                        st.success(
                            f"Metadata loaded from {metadata_path} successfully! found {len(metadata)} Images"
                        )
                except Exception as e:
                    st.error(f"Error occurred while loading metadata: {str(e)}")
            else:
                st.warning("Please provide the metadata file path.")
