# QTI Quiz - Factor Analysis

This folder contains a comprehensive 25-question quiz on Factor Analysis and Principal Component Analysis, formatted for conversion to QTI (Question & Test Interoperability) format.

## Contents

- `factor_analysis_quiz.txt` - Quiz questions in txttoqti educational format
- `README.md` - This documentation file

## Quiz Coverage

The quiz comprehensively covers all major topics from the Factor Analysis study guide:

### Topic Distribution:
- **PCA Theory & Implementation** (Questions 1, 7, 16, 17, 20) - 5 questions
- **Factor Analysis Fundamentals** (Questions 2, 8, 11, 12, 16) - 5 questions  
- **Practical Implementation** (Questions 4, 5, 6, 9, 10) - 5 questions
- **Rotation & Interpretation** (Questions 3, 13, 15, 18, 19) - 5 questions
- **Advanced Topics & Applications** (Questions 14, 21, 22, 23, 24, 25) - 5 questions

### Question Types:
- Conceptual understanding
- Methodological decisions
- Interpretation of results
- Statistical criteria and thresholds
- Software implementation considerations

## How to Convert to QTI Format

### Prerequisites:
```bash
# Install txttoqti (already installed in this project)
uv add txttoqti
```

### Conversion Command:
```bash
# Navigate to the quiz folder
cd evaluations/4_Factor_Analysis/qti_quiz/

# Convert to QTI ZIP file
uv run txttoqti -i factor_analysis_quiz.txt -o factor_analysis_quiz.zip
```

### Alternative Python API:
```python
import txttoqti

# Convert using Python API
converter = txttoqti.TxtToQti()
converter.read_txt("factor_analysis_quiz.txt").save_to_qti("factor_analysis_quiz.zip")
```

## LMS Import Instructions

### Canvas:
1. Go to your course → Quizzes
2. Click "New Quiz"
3. Click "Import Quiz"
4. Upload the generated ZIP file
5. Configure quiz settings (time limit, attempts, etc.)

### Moodle:
1. Go to course → Turn editing on
2. Add an activity → Quiz
3. Quiz settings → Import → QTI format
4. Upload the ZIP file
5. Configure quiz parameters

### Blackboard:
1. Go to course → Assessments → Tests
2. Create Test → Import Test
3. Select QTI Package
4. Upload ZIP file

## Quiz Specifications

- **Number of Questions:** 25
- **Question Type:** Multiple choice (4 options each)
- **Difficulty Level:** Mixed (introductory to advanced)
- **Estimated Time:** 45-60 minutes
- **Recommended Attempts:** 2-3 (for learning purposes)

## Answer Key Summary

Questions with correct answers:
- Conceptual questions focus on understanding core differences between PCA and FA
- Methodological questions test knowledge of when to apply specific techniques
- Interpretation questions assess ability to read and understand results
- Statistical questions verify knowledge of thresholds and criteria

## Usage Recommendations

### For Formative Assessment:
- Allow multiple attempts
- Provide immediate feedback
- Use as study tool alongside lecture notes

### For Summative Assessment:
- Single attempt
- Time limit: 60 minutes
- Randomize question order
- Combine with practical analysis component

## Quality Assurance

- All questions reviewed for accuracy against study guide content
- Answer choices designed to test common misconceptions
- Balanced coverage across all major topics
- Questions aligned with learning objectives

---
**Created:** September 2025  
**Based on:** Factor Analysis Study Guide v1.0  
**Format:** txttoqti educational format  
**Target LMS:** Canvas, Moodle, Blackboard (QTI 2.1 compatible)
