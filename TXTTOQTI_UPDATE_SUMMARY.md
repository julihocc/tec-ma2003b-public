# txttoqti v0.6.0 Update Summary

## Overview
Successfully updated txttoqti dependency from PyPI version 0.5.0 to GitHub latest release v0.6.0, which includes major new features not yet published to PyPI.

## Changes Made

### 1. Updated `pyproject.toml`
- Changed dependency from `txttoqti>=0.5.0` to `txttoqti @ git+https://github.com/julihocc/txttoqti.git@v0.6.0`
- Adjusted version requirements to be compatible with Python 3.10:
  - `matplotlib>=3.8.0` (was 3.10.6)
  - `numpy>=1.24.0` (was 2.3.3)
  - `pandas>=2.0.0` (was 2.3.2)
  - `scikit-learn>=1.3.0` (was 1.7.2)
  - `seaborn>=0.12.0` (was 0.13.2)

### 2. Updated Quiz README
Updated `evaluations/4_Factor_Analysis/qti_quiz/README.md` to document new v0.6.0 features:
- Added QTI version selection commands
- Updated CLI examples with proper syntax
- Added Python API examples with new `TxtToQtiConverter`
- Added version information in footer

### 3. Installation & Testing
- Successfully installed txttoqti v0.6.0 from GitHub
- Tested both QTI 1.2 (Canvas compatible) and QTI 2.1 (modern standard) conversion
- Verified both CLI and Python API functionality

## New Features Available in v0.6.0

### QTI Version Selection
- **QTI 1.2**: Canvas LMS compatible format (default)
- **QTI 2.1**: Modern QTI standard
- CLI parameter: `--qti-version qti12|qti21`

### Enhanced CLI Interface
- Better error handling and user feedback
- Auto-generated output filenames with timestamps
- Backward compatibility maintained

### CSV Format Support
- Scantron format parsing
- Automatic format detection
- Seamless integration with existing workflow

## Usage Examples

### CLI Commands
```bash
# Canvas LMS compatible (QTI 1.2)
txttoqti -i questions.txt --qti-version qti12

# Modern QTI standard (QTI 2.1)
txttoqti -i questions.txt --qti-version qti21

# Custom output file
txttoqti -i questions.txt -o custom.zip --qti-version qti12
```

### Python API
```python
from txttoqti import TxtToQtiConverter

converter = TxtToQtiConverter()
result = converter.convert_file('questions.txt', qti_version='qti12')
```

## Testing Results
- ✅ txttoqti v0.6.0 successfully installed from GitHub
- ✅ QTI 1.2 conversion tested and working
- ✅ QTI 2.1 conversion tested and working
- ✅ Python API import successful
- ✅ Generated files: `factor_analysis_quiz-TIMESTAMP-qti12.zip` and `factor_analysis_quiz-TIMESTAMP-qti21.zip`

## Next Steps
- Consider updating other quiz files in the project to use new QTI version selection
- Monitor for PyPI release of v0.6.0 to potentially switch back to PyPI version
- Update any automation scripts to use new CLI syntax