# 🚀 CareerseekAI Backend (AWS Serverless with Terraform)

CareerseekAI is an AI-powered job search assistant that helps users **find, track, and apply to jobs** with **AI-based recommendations** and **automated workflows**.

The backend is built with **FastAPI**, deployed on **AWS Lambda** via **API Gateway**, and uses **Amazon RDS (PostgreSQL)** for persistent storage.  
Infrastructure is managed with **Terraform**.

---

## 🎯 Goal
- Manage user authentication and profiles
- Store and manage jobs
- Track applications and statuses
- Provide AI-powered job matching and cover letter generation (future)
- Support job scraping and auto-apply features (future)

---

## ☁️ AWS Architecture
- **API Gateway** → **AWS Lambda (FastAPI via Mangum)**
- **Amazon RDS (PostgreSQL)** for database
- **AWS Secrets Manager** for database credentials
- **Amazon S3** (future) for resumes/uploads
- **Amazon Bedrock / OpenAI API** for AI features

---

## 🛠 Tech Stack
- **Framework:** FastAPI (Python)
- **Deployment:** AWS Lambda + API Gateway
- **Database:** PostgreSQL (Amazon RDS)
- **ORM:** SQLAlchemy (Async)
- **Authentication:** JWT (PyJWT)
- **Secrets:** AWS Secrets Manager
- **Infrastructure as Code:** Terraform
- **CI/CD:** GitHub Actions (optional)

---

## 📂 Project Structure
careerseekai-backend/
│── app/
│   ├── main.py            # FastAPI entry
│   ├── config.py          # DB config (reads from Secrets Manager)
│   ├── database.py        # SQLAlchemy connection
│   ├── models/            # SQLAlchemy models
│   ├── schemas/           # Pydantic schemas
│   ├── routers/           # API routes
│   └── auth/              # JWT auth logic
│
│── infra/                 # Terraform IaC
│   ├── main.tf            # Lambda, API Gateway, RDS, Secrets Manager
│   ├── variables.tf
│   ├── outputs.tf
│   └── backend.tf
│
│── requirements.txt
│── README.md

---

## 📡 API Endpoints (MVP)

| Method | Endpoint             | Description                          |
|--------|----------------------|--------------------------------------|
| POST   | /auth/register       | Register new user                   |
| POST   | /auth/login          | Login & get JWT                     |
| GET    | /jobs                | Get all jobs for user               |
| POST   | /jobs                | Add a job                           |
| PUT    | /jobs/{id}           | Update job details                  |
| DELETE | /jobs/{id}           | Delete a job                        |
| POST   | /applications        | Save application status             |
| GET    | /applications        | List all applications for user      |
| PUT    | /applications/{id}   | Update application status           |

---

## 🛣️ Roadmap

### ✅ **Phase 1 – MVP (Backend + AWS Lambda)**
- Set up FastAPI project with Mangum
- Connect to PostgreSQL (Amazon RDS)
- Implement JWT authentication
- CRUD APIs for Users, Jobs, Applications

### 🔹 **Phase 2 – Dashboard Integration**
- Expose endpoints for frontend
- Add search/filter for jobs
- Add analytics endpoints (applied vs. interview stats)

### 🔹 **Phase 3 – AI Integration**
- AI-based job match scoring (OpenAI/Amazon Bedrock)
- Auto-generated tailored cover letters

### 🔹 **Phase 4 – Automation**
- Job scraping with Lambda scheduled jobs
- Auto-save scraped jobs
- Auto-apply feature

---

## 🚀 Deployment Guide (Terraform)

### **1️⃣ Prerequisites**
- Install Terraform → [https://developer.hashicorp.com/terraform/downloads](https://developer.hashicorp.com/terraform/downloads)
- Install AWS CLI → `brew install awscli` (Mac)
- Configure AWS credentials:
```bash
aws configure