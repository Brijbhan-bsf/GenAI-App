# Assignment 39: GenAI App Deployment

**Student:** Brijbhan Kumar

## Problem Statement

Deploy a GenAI application so that users can access it online.

This project demonstrates a Streamlit application prepared for deployment on:

1. Streamlit Cloud
2. Hugging Face Spaces

## Project Files

```text
GenAI-Task39-BrijbhanKumar/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Task 1: Deployment on Streamlit Cloud

### Step 1: Push the project to GitHub

Create a new GitHub repository and upload all project files.

Example repository structure:

```text
repository/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Step 2: Deploy on Streamlit Cloud

1. Open Streamlit Community Cloud.
2. Sign in with GitHub.
3. Select **Create app**.
4. Select the GitHub repository.
5. Select the branch containing the project.
6. Set the main file to:

```text
app.py
```

7. Click **Deploy**.
8. Wait for the application to build.
9. Open the generated public URL.

### Step 3: Test the live application

Test the following:

- Application loads successfully.
- Text can be entered.
- **Analyze Text** button works.
- Word count is displayed.
- Character count is displayed.
- Line count is displayed.

**Streamlit Cloud Live URL:**  
(https://genai-app-3htapec67tsdhc2tbim7ts.streamlit.app/)

## Task 2: Deployment on Hugging Face Spaces

### Step 1: Create a Space

1. Sign in to Hugging Face.
2. Create a new Space.
3. Select **Streamlit** as the SDK.
4. Choose the appropriate visibility.
5. Create the Space.

### Step 2: Upload or connect the project

Upload:

```text
app.py
requirements.txt
README.md
```

The Space should use `app.py` as the Streamlit application.

### Step 3: Configure README.md

This repository already contains a README suitable for documenting the project.

The Hugging Face Space README can also contain Space metadata at the top. If Hugging Face asks for a Space configuration block, use:

```yaml
---
title: GenAI App Deployment
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.38.0
app_file: app.py
pinned: false
---
```

### Step 4: Deploy and test

After uploading the files:

1. Wait for the Space to build.
2. Open the running application.
3. Enter sample text.
4. Click **Analyze Text**.
5. Verify the output.

**Hugging Face Spaces URL:**  
`PASTE-YOUR-HUGGING-FACE-SPACE-URL-HERE`

## Task 3: Compare Deployment Platforms

### 1. Streamlit Cloud vs Hugging Face Spaces

| Feature | Streamlit Cloud | Hugging Face Spaces |
|---|---|---|
| Main focus | Streamlit applications | ML/AI and demo applications |
| Deployment | GitHub-based workflow | GitHub or direct file upload |
| Streamlit support | Native | Supported |
| AI/ML ecosystem | Good | Strong AI/ML ecosystem |
| GitHub integration | Strong | Available |
| Public demos | Yes | Yes |
| Best suited for | Streamlit data/AI apps | AI/ML demos and model-related applications |

### 2. Pros and Cons

#### Streamlit Cloud

**Pros**
- Simple deployment for Streamlit applications
- Strong GitHub workflow
- Easy application management
- Designed specifically around Streamlit

**Cons**
- Mainly focused on Streamlit applications
- Resource limitations can affect larger applications
- Advanced infrastructure may require another hosting solution

#### Hugging Face Spaces

**Pros**
- Strong AI/ML community and ecosystem
- Good platform for sharing AI demonstrations
- Supports Streamlit and other application frameworks
- Convenient for ML and GenAI projects

**Cons**
- Free resources are limited
- Build/runtime behavior depends on the selected Space hardware and configuration
- Some applications may require paid resources for larger workloads

### 3. When to use which?

**Use Streamlit Cloud when:**
- The application is primarily a Streamlit application.
- You want a simple GitHub-to-deployment workflow.
- The project is a dashboard, data app, or lightweight GenAI application.

**Use Hugging Face Spaces when:**
- The application is closely related to AI/ML.
- You want to share an AI demonstration with the Hugging Face community.
- You may want to combine the application with Hugging Face models or resources.

## Deployment Validation Checklist

### Streamlit Cloud

- [ ] GitHub repository created
- [ ] `app.py` uploaded
- [ ] `requirements.txt` uploaded
- [ ] Streamlit Cloud deployment completed
- [ ] Live URL opened
- [ ] Application tested

### Hugging Face Spaces

- [ ] Space created
- [ ] Streamlit SDK selected
- [ ] `app.py` uploaded
- [ ] `requirements.txt` uploaded
- [ ] `README.md` configured
- [ ] Space deployed
- [ ] Application tested

## Sample Test Input

```text
Generative AI applications can be deployed online so users can access them through a web browser.
```

Expected result:

- The application displays a word count.
- The application displays a character count.
- The application displays a line count.

## Conclusion

The application has been prepared for deployment on both Streamlit Cloud and Hugging Face Spaces. Both platforms provide practical ways to make Streamlit-based AI applications accessible through a web interface. The appropriate platform depends on the application's requirements, ecosystem, deployment workflow, and resource needs.
