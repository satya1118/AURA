# Technical Overview

AURA is built on a **multimodal risk scoring pipeline** combining structured data, text, and visual signals.  
This document describes the technical architecture, data flow, and modeling approach.

---

# 🧩 System Architecture

AURA integrates five major layers:

1. **Data Ingestion Layer**  
2. **Feature Store (Feast)**  
3. **Modeling Layer (XGBoost + LLM + CV)**  
4. **Serving Layer (FastAPI services)**  
5. **UX Layer (Dashboard + Risk Map)**  

The diagram below represents the architecture at a high level:

<p align="center">
  <img src="assets/architecture.png" width="850">
</p>

---

## 1. Data Sources

AURA processes multiple independent signals:

### **Structured signals**
- Time of day  
- Location grid (geohash)  
- Weather conditions  
- Traffic density  
- Event schedules  

### **Text signals**
- 911 call descriptions  
- Operator notes  
- Social text clusters (simulated)

Processed with a small **LLM classifier** to derive incident urgency + category.

### **Visual signals**
- CCTV activity spikes  
- Motion anomalies  
- Crowd density approximations

---

## 2. Ingestion & Feature Engineering

AURA supports:

### **Real-time streaming (simulated)**
- Kafka-like ingestion pipeline  
- Sliding-window feature generation  

### **Batch ETL**
- Enrichment from external APIs  
- Weather + Event merging  
- Time-series tagging  

### Feature Types  
- Historical lag features  
- Rolling windows  
- Spatial neighborhood aggregations  
- Text embeddings  
- CCTV anomaly frequencies  

Architecture supports **online + offline** feature parity through Feast.

---

## 3. Modeling Layer

AURA uses a **hybrid ensemble**:

### **A. XGBoost — Structured Classifier**
Predicts risk level using tabular + geospatial engineered features.

### **B. LLM Classifier — Text Reasoning**
Summarizes 911 call descriptions and operator notes into:
- Event type  
- Severity  
- Latent risk factors  

### **C. CV Spike Detector — Visual Data**
Identifies sudden motion/activity spikes from CCTV signals (simulated).

### **Model Fusion**
Outputs from all models are weighted and aggregated into the final risk score.

---

## 4. Serving Layer

AURA exposes:

- `/predict` endpoint — returns risk score, SHAP explanation, and rationale  
- `/hotspots` — returns ranked geospatial hotspots  
- `/events` — returns anomaly clusters  

Powered by **FastAPI**, enabling ~150 ms inference on typical workloads.

---

## 5. UX Layer

The primary operator interface includes:

- Chicago risk heatmap  
- Hotspot rings  
- Risk tiers  
- SHAP explanations  
- Anomaly clusters  
- Tactical recommendations  

Built as an HTML prototype in the `/prototype/` folder.

---

# 🧪 Simulation Notebook

The notebook demonstrates:

- Data generation  
- Feature creation  
- Model training  
- SHAP value computation  
- Hotspot mapping  
- Synthetic pilot results  

Located in:

```
notebooks/AURA_simulation_advanced.ipynb
```

---

# ⚙️ Technical Tradeoffs

- Used XGBoost for interpretability + speed (over deep learning)  
- LLM used lightly to avoid latency issues  
- CV model simulated to avoid compute-heavy pipelines  
- Feast feature store chosen for online/offline parity  
- FastAPI chosen for simplicity + production alignment  

---

# 🔐 Responsible AI Practices

- No demographic variables  
- Neighborhood bias checks  
- SHAP explanations for transparency  
- Human-in-loop review required  
- Compliance-ready architecture  

---

# 🧭 Future Enhancements

- Real CCTV integration  
- Deep sequence models (Temporal Transformers)  
- Multicity model generalization  
- Real-time patrol routing with RL  
- Streaming LLM summarization  

AURA’s architecture is designed for **scalability, modularity, and safe real-world deployment**.

