## **Ethiopian Medical Data Warehouse**

This project is a comprehensive pipeline for extracting, transforming, and exposing Ethiopian medical business data for analytics and object detection. The system leverages advanced tools like **Telethon**, **YOLOv5**, **DBT**, and **FastAPI** to automate data collection, transformation, and analysis.

---

### **Features**
1. **Telegram Data Scraping**: Collect data and images from Telegram channels using **Telethon**.
2. **Object Detection**: Use **YOLOv5** to perform object detection on scraped images.
3. **Data Transformation and Warehouse**: Transform and store cleaned data using **DBT** and PostgreSQL.
4. **API Exposure**: Build an API to access and manage data using **FastAPI**.

---

### **How the Project Works**

#### **1. Data Scraping**
- Telegram channels like `https://t.me/lobelia4cosmetics` are scraped using the Telethon API.
- Images and text data are saved locally for further processing.
- **Tools Used**: Telethon, Python.

#### **2. Object Detection**
- YOLOv5 pre-trained models detect objects in scraped images.
- Bounding box coordinates, class labels, and confidence scores are extracted.
- Detection results are saved as a CSV and stored in a PostgreSQL database.
- **Tools Used**: YOLOv5, PyTorch, PostgreSQL.

#### **3. Data Transformation**
- Raw data is transformed into analytics-ready datasets using **DBT**.
- DBT models standardize and clean data for efficient querying.
- Data is tested for quality and documented for clarity.
- **Tools Used**: DBT, PostgreSQL.

#### **4. API Exposure**
- FastAPI provides RESTful endpoints to access and manage the medical business data.
- Users can create, retrieve, and query data through the API.
- **Tools Used**: FastAPI, SQLAlchemy, Pydantic.

---

### **Future Improvements**
- Add user authentication to the API for secure data access.
- Include more advanced data visualizations and analytics.
- Automate data scraping and model updates with a scheduler like **Airflow**.

---

### **Acknowledgements**
This project uses:
- **Telethon** for Telegram scraping.
- **YOLOv5** for object detection.
- **DBT** for data transformation.
- **FastAPI** for API exposure.
