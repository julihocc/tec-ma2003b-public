# txttoqti v0.7.0 Update Summary

## Overview
Successfully updated txttoqti dependency from v0.6.0 to GitHub latest release v0.7.0, which introduces comprehensive Multiple Response Question support and enhanced functionality.

## Changes Made

### 1. Updated `pyproject.toml`
- Changed dependency from `txttoqti @ git+https://github.com/julihocc/txttoqti.git@v0.6.0` to `txttoqti @ git+https://github.com/julihocc/txttoqti.git@v0.7.0`
- Version requirements remain compatible with Python 3.10:
  - `matplotlib>=3.8.0`
  - `numpy>=1.24.0`
  - `pandas>=2.0.0`
  - `scikit-learn>=1.3.0`
  - `seaborn>=0.12.0`

### 2. Updated Quiz README
Updated `evaluations/4_Factor_Analysis/qti_quiz/README.md` to document new v0.7.0 features:
- Added Multiple Response Question documentation
- Updated CLI examples with MR question format
- Added POINTS: line support documentation
- Updated version information to reflect v0.7.0

### 3. Installation & Testing
- Successfully installed txttoqti v0.7.0 from GitHub
- Tested Multiple Response Questions with both QTI 1.2 and QTI 2.1
- Created sample MR quiz file: `multiple_response_test.txt`
- Verified both CLI and Python API functionality with new features

## New Features Available in v0.7.0

### Multiple Response Questions (NEW)
- **Full MR Support**: Complete implementation of "Select all that apply" questions
- **Comma-separated Answers**: Support for multiple correct answers (e.g., "A,C,E")
- **Proper QTI Generation**: Correct `rcardinality="Multiple"` attribute in QTI 1.2
- **Enhanced Validation**: Validates multiple response questions with multiple correct answers

### Enhanced CSV Parsing
- **Extended Scantron Format**: A-E choices (previously limited to A-D)
- **Comma-separated Answer Parsing**: Support for "2,4" format (choices B and D)
- **Mixed Question Types**: Handle both MC and MR questions in same file

### Custom Points Support
- **POINTS Line**: Specify custom point values per question
- **Proper QTI Handling**: Uses actual question points instead of hardcoded values
- **Educational Format Extension**: Enhanced metadata support

### Technical Improvements
- **MULTIPLE_RESPONSE Enum**: New question type in QuestionType enumeration
- **Enhanced Validation**: Dedicated `_validate_multiple_response()` method
- **QTI12Generator Updates**: Proper cardinality handling for multiple response questions

## Usage Examples

### CLI Commands
```bash
# Multiple Response Questions (NEW v0.7.0)
txttoqti -i multiple_choice_and_response.txt --qti-version qti12

# Canvas LMS compatible (QTI 1.2)
txttoqti -i questions.txt --qti-version qti12

# Modern QTI standard (QTI 2.1)
txttoqti -i questions.txt --qti-version qti21

# Custom output file
txttoqti -i questions.txt -o custom.zip --qti-version qti12
```

### Multiple Response Question Format
```
Q1: Which are correct? (Select all that apply)
A) Option 1
B) Option 2
C) Option 3
D) Option 4
ANSWER: A,C

POINTS: 3
Q2: Advanced question with custom points
A) Choice A
B) Choice B
ANSWER: A,B
```

### Python API
```python
from txttoqti import TxtToQtiConverter

converter = TxtToQtiConverter()
result = converter.convert_file('questions.txt', qti_version='qti12')
```

## Testing Results
- ✅ txttoqti v0.7.0 successfully installed from GitHub
- ✅ Multiple Response Questions tested and working (QTI 1.2 and 2.1)
- ✅ Mixed MC/MR question files converted successfully
- ✅ POINTS: line support verified
- ✅ Python API compatibility confirmed
- ✅ Generated files: `multiple_response_test-TIMESTAMP-qti12.zip` and `multiple_response_test-TIMESTAMP-qti21.zip`

## Next Steps
- Create more Multiple Response questions for comprehensive course assessments
- Update existing quiz files to leverage new MR functionality where appropriate
- Consider using custom POINTS: lines for weighted questions
- Monitor for PyPI release of v0.7.0 to potentially switch back to PyPI version
- Update any automation scripts to leverage new Multiple Response features