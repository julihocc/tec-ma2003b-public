# MA2003B Course Evaluations

This repository contains evaluation materials for the MA2003B Multivariate Analysis course.

**IMPORTANT: This repository should remain PRIVATE**

## Structure

Following the same organization as the main lessons repository:

```
evaluations/
├── README.md
└── 4_Factor_Analysis/
    ├── qti_quiz/              # QTI format quiz using txttoqti
    └── business_case_study/   # Business case study assignment
```

## Dependencies

- `txttoqti` for QTI quiz generation: https://pypi.org/project/txttoqti/

## Usage

Each chapter folder contains:
- QTI quiz materials for online assessment platforms
- Business case studies for practical application

## Quick Start

### Convert Quiz to QTI Format:
```bash
cd evaluations/4_Factor_Analysis/qti_quiz/
uv run txttoqti -i factor_analysis_quiz.txt -o factor_analysis_quiz.zip
```

### Import to LMS:
Upload the generated ZIP file to Canvas, Moodle, or Blackboard.

---
**Repository Type:** Private Submodule  
**Parent Repository:** tec-ma2003b-public
