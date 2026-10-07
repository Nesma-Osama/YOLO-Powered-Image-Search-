# 🔎 YOLO-Powered Image Search

A computer vision application that uses **YOLO object detection** to analyze images and enables users to search for images based on the objects detected in them.

The application is built with **Python and Streamlit** and provides an interactive interface for processing images, generating detection metadata, and searching through images using detected object classes.

---

## ✨ Features

* 🎯 **YOLO-based object detection**
* 🔍 Search images using detected object classes
* 🔗 Support for **AND / OR search logic**
* 📊 Generate and store detection metadata
* 🖼️ Display image search results
* 📦 Count unique detected object classes
* ⚡ Reuse saved metadata instead of performing unnecessary inference
* 🌐 Interactive **Streamlit** web interface
* 📁 Organized and reusable inference and utility modules

---

## 🧠 How It Works

The application follows a simple pipeline:

```text
             Input Images
                  │
                  ▼
          ┌───────────────┐
          │ YOLO Inference│
          └───────┬───────┘
                  │
                  ▼
          Detection Results
                  │
                  ▼
          Metadata Generation
                  │
                  ▼
          ┌───────────────┐
          │ Image Search  │
          │   AND / OR    │
          └───────┬───────┘
                  │
                  ▼
            Search Results
```

### 1. Image Detection

The application uses YOLO to process the images and identify objects present in each image.

For every detected object, information such as its class and detection result can be used to describe the image.

### 2. Metadata

Instead of running object detection every time a user performs a search, the application can save and load metadata associated with the processed images.

This allows the search process to work with previously generated detection information.

### 3. Image Search

Users can search for images based on the detected object classes.

The application supports two search modes:

**AND**

Returns images that contain **all** of the selected classes.

```text
person AND car
```

The returned images must contain both a person and a car.

**OR**

Returns images that contain **at least one** of the selected classes.

```text
person OR car
```

The returned images can contain a person, a car, or both.

---

## 🛠️ Technologies Used

| Technology    | Purpose                     |
| ------------- | --------------------------- |
| **Python**    | Main programming language   |
| **YOLO**      | Object detection            |
| **Streamlit** | Interactive web application |
| **OpenCV**    | Image processing            |
| **NumPy**     | Numerical operations        |

---

## 📁 Project Structure

```text
YOLO-Powered-Image-Search/
│
├── app.py
│
├── src/
│   ├── inference.py
│   └── utils.py
│
├── requirements.txt
│
└── README.md
```

### Main Components

#### `app.py`

The main Streamlit application.

It handles:

* User interface
* Session state
* Image search
* Search options
* Displaying results

#### `src/inference.py`

Contains the YOLO inference functionality used to process images and obtain detection results.

#### `src/utils.py`

Contains utility functions used by the application, including functionality related to:

* Saving metadata
* Loading metadata
* Finding unique classes and their counts
* Preparing image results

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Nesma-Osama/YOLO-Powered-Image-Search-.git
```

Navigate to the project directory:

```bash
cd YOLO-Powered-Image-Search-
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

After running the command, Streamlit will provide a local URL where you can access the application in your browser.

---
