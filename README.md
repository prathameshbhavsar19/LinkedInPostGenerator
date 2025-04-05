# GenAI Post Generator

This project is a LinkedIn post generation tool designed specifically for influencers. By analyzing an influencer's past posts, the tool learns their writing style and helps generate new posts that align with their personal tone, preferred topics, and audience engagement style.

## Overview

**GenAI Post Generator** enables a LinkedIn influencer (e.g., Mohan) to:
- Feed in past LinkedIn posts.
- Automatically extract metadata such as topic, language, and length.
- Select preferences for a new post (topic, length, language).
- Generate a new post that mimics the writing style from previous posts using few-shot learning with a Large Language Model (LLM).

## Architecture

The tool works in two main stages:

### Stage 1: Post Preprocessing
- Collects past LinkedIn posts.
- Extracts metadata such as:
  - Topic
  - Language
  - Length
- Stores this structured information for later filtering and use.

### Stage 2: Post Generation
- User selects the topic, language, and post length.
- The system finds a few past examples matching those filters.
- These examples are used as context (few-shot learning) to generate a new post with similar style and tone.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/project-genai-post-generator.git
cd project-genai-post-generator
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Key
- Visit [Groq Console](https://console.groq.com/keys) to create an API key.
- Create a `.env` file in the root directory and add your key:
```
GROQ_API_KEY=your_api_key_here
```

### 5. Run the Streamlit App
```bash
streamlit run main.py
```

The app will open in your browser. From there, you can explore, filter, and generate new LinkedIn posts.

## Project Goals

- Learn and replicate an influencer's writing style using few-shot examples.
- Speed up the post creation process while retaining authenticity.
- Support creative ideation for content creators on LinkedIn.

## License and Usage

This project is licensed under the MIT License.  
**However, commercial use of this software is strictly prohibited without prior written permission from the author.**  
Attribution must be given in all copies or substantial portions of the software.