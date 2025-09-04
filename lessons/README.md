# Course Lessons Directory

This directory contains all course materials for MA2003B - Análisis Multivariado, with a focus on modern presentation systems using Typst.

## 📚 Documentation

### Quick Start
- **[TYPST_CHEATSHEET.md](TYPST_CHEATSHEET.md)** - Essential Typst commands and syntax reference
- **[TYPST_GUIDE.md](TYPST_GUIDE.md)** - Comprehensive guide to Typst for course development

### Templates
- **[Course Presentation Template](shared/templates/course_presentation_template.typ)** - Ready-to-use presentation template

## 📖 Current Lessons

### Chapter 4: Factor Analysis ✅ Complete
- **Location**: `4_Factor_Analysis/beamer/`
- **Main File**: `factor_analysis_presentation.typ` 
- **Status**: Fully migrated from LaTeX to Typst
- **Topics**: PCA, Factor Analysis, 4 comprehensive examples, method comparisons

## 🚀 Getting Started with Typst

### 1. Installation Check
```bash
# Verify Typst is installed
~/.local/bin/typst --version
```

### 2. Create New Presentation
```bash
# Copy template
cp lessons/shared/templates/course_presentation_template.typ my_presentation.typ

# Edit content (use VS Code with Typst extensions)
code my_presentation.typ

# Compile
typst compile my_presentation.typ
```

### 3. Development Workflow
```bash
# Watch mode (auto-compile on changes)
typst watch my_presentation.typ

# Open PDF viewer (will auto-refresh)
evince my_presentation.pdf &
```

## 📋 Migration Status

### Completed ✅
- [x] **Factor Analysis** - Full presentation (419 slides → Typst)
- [x] **Performance improvement** - 47x faster compilation (9.4s → 0.2s)
- [x] **Template system** - Reusable course presentation template
- [x] **Documentation** - Complete guides and cheat sheets

### Future Chapters (To be developed)
- [ ] **Multivariate Regression**
- [ ] **Discriminant Analysis** 
- [ ] **Cluster Analysis**
- [ ] **Advanced Topics**

## 🎯 Key Benefits Achieved

| Aspect | LaTeX | Typst | Improvement |
|--------|--------|--------|-------------|
| **Compilation Speed** | 9.4 seconds | 0.2 seconds | 47x faster |
| **Error Messages** | Cryptic | Clear & helpful | Much better |
| **Syntax** | Complex | Clean & readable | Easier maintenance |
| **Learning Curve** | Steep | Gentle | Faster onboarding |
| **File Size** | 838KB | 103KB | Smaller output |

## 📁 Directory Structure

```
lessons/
├── README.md                          # This overview
├── TYPST_GUIDE.md                     # Complete Typst guide
├── TYPST_CHEATSHEET.md               # Quick reference
├── shared/
│   └── templates/
│       └── course_presentation_template.typ
├── 4_Factor_Analysis/                 # ✅ Complete
│   ├── README.md                      # Chapter-specific docs
│   ├── beamer/
│   │   ├── factor_analysis_presentation.typ    # Main Typst file
│   │   ├── factor_analysis_presentation.pdf    # Generated PDF
│   │   ├── legacy_latex/                       # Preserved LaTeX
│   │   └── old_artifacts/                      # Build artifacts
│   └── code/                          # Python examples
└── [future chapters]/
```

## 🔧 VS Code Setup (Recommended)

1. **Install Extensions**:
   - "Typst LSP" - Language server support
   - "Typst Preview" - Live preview

2. **Keybinding**: Ctrl+Shift+P → "Typst Preview" 

3. **Workflow**:
   - Edit `.typ` file in VS Code
   - See live preview in sidebar
   - PDF updates automatically

## 💡 Best Practices

### File Organization
- Use the template for new presentations
- Keep presentation-specific assets in same directory
- Preserve LaTeX files in `legacy_` folders during migration

### Content Development
- Start with template structure
- Use `#slide(title: [Title])[content]` for regular slides
- Use `#section-slide[Title]` for section dividers
- Test compilation frequently during development

### Collaboration
- Typst files are plain text (version control friendly)
- Share `.typ` files and generated PDFs
- Use consistent formatting and functions

## 📞 Getting Help

- **Quick answers**: See [TYPST_CHEATSHEET.md](TYPST_CHEATSHEET.md)
- **Detailed guide**: See [TYPST_GUIDE.md](TYPST_GUIDE.md)
- **Template example**: `shared/templates/course_presentation_template.typ`
- **Working example**: `4_Factor_Analysis/beamer/factor_analysis_presentation.typ`

## 🎉 Success Story

The Factor Analysis chapter demonstrates the full potential of migrating to Typst:
- **419 slides** successfully migrated
- **All mathematical content** properly rendered
- **47x faster compilation** 
- **Professional output** maintained
- **Legacy preserved** for future reference

This establishes Typst as the recommended system for future course development.