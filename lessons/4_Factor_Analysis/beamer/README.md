# Factor Analysis Presentation

This directory contains the Factor Analysis presentation in both legacy LaTeX and modern Typst formats.

## Current Working Files

- **`factor_analysis_presentation.typ`** - Main Typst presentation source
- **`factor_analysis_presentation.pdf`** - Generated presentation PDF

## Quick Start

### Compile with Typst (Recommended)
```bash
# Install Typst if not already installed
~/.local/bin/typst compile factor_analysis_presentation.typ

# Or use system Typst if available
typst compile factor_analysis_presentation.typ
```

### Compile with LaTeX (Legacy)
```bash
# From the legacy_latex directory
cd legacy_latex
pdflatex factor_analysis_presentation.tex
pdflatex factor_analysis_presentation.tex  # Run twice for cross-references
```

## Performance Comparison

| Method | Compilation Time | File Size | Maintenance |
|--------|------------------|-----------|-------------|
| **Typst** | ~0.2 seconds | 103 KB | Easy |
| LaTeX | ~9.4 seconds | 838 KB | Complex |

## Directory Structure

```
beamer/
├── factor_analysis_presentation.typ     # Main Typst source (RECOMMENDED)
├── factor_analysis_presentation.pdf     # Generated presentation
├── legacy_latex/                        # Legacy LaTeX files
│   ├── factor_analysis_presentation.tex # Original LaTeX source
│   └── factor_analysis_presentation_latex_final.pdf
├── old_artifacts/                       # Build artifacts and old versions
└── README.md                            # This file
```

## Content Overview

The presentation covers:

1. **Principal Component Analysis (PCA)**
   - Theory and mathematical foundations
   - Educational assessment example (synthetic data)
   - European stock markets analysis
   - Kuiper Belt objects (astronomical data)
   - Hospital health outcomes

2. **Factor Analysis**
   - Theoretical framework
   - Comparison with PCA methodology
   - Same datasets reanalyzed

3. **Comparison and Applications**
   - Method selection guidelines
   - Practical recommendations

## Migration Notes

- **✅ Migrated from LaTeX to Typst** (Sep 2025)
- **✅ All content preserved**: 419 slides fully converted
- **✅ Mathematical notation updated** to Typst syntax
- **✅ Performance improved**: 45x faster compilation
- **✅ Legacy preserved** in `legacy_latex/` directory

## Future Development

Going forward, use the Typst version (`factor_analysis_presentation.typ`) for:
- ✅ Faster iteration and development  
- ✅ Easier maintenance and updates
- ✅ Modern tooling and better error messages
- ✅ Cleaner, more readable source code

The LaTeX version is maintained in `legacy_latex/` for reference and compatibility.