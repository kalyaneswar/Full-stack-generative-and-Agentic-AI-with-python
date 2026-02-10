<!-- Types of promting  -->

# Prompting Basics

This document explains common **types of prompting** and **prompt serialization formats** in simple words.

---

## 🧠 Types of Prompting

Prompting is the way we give instructions to an AI model so it understands what to do.

---

### 1. Zero-Shot Prompting
The model is asked a question **without giving any examples**.

**Example:**

**Use case:** Simple and common tasks.

---

### 2. One-Shot Prompting
The model is given **one example** before asking the actual question.

**Example:**

**Use case:** Helps the model understand the pattern.

---

### 3. Few-Shot Prompting
The model is given **multiple examples**.

**Example:**

**Use case:** Useful for complex or customized tasks.

---

### 4. Chain-of-Thought Prompting
The model is asked to **think step by step** before answering.

**Example:**

**Use case:** Improves reasoning for math, logic, and problem-solving.

---

### 5. Persona-Based Prompting
The model is instructed to **act as a specific role or persona**.

**Example:**

**Use case:** Produces more relevant and role-specific responses.

---

## 📦 Prompt Serialization Formats

Prompt serialization defines **how prompts are structured and formatted** before sending them to the model.

---

### 1. Alpaca Format
Uses a clear **instruction + input + output** structure.

**Example:**

**Best for:** Instruction-tuned models and datasets.

---

### 2. ChatML Format
Uses **roles** such as system, user, and assistant.

**Example:**
```json
[
  { "role": "system", "content": "You are a helpful assistant" },
  { "role": "user", "content": "Explain Docker" }
]
```

### 3. INST Format (Instruction Format)

INST format is a **simple and compact way** to give direct instructions to the model.  
The instruction is wrapped inside special tags.

**Format:**


