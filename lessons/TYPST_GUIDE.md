# Typst Guide for Course Development

This guide explains how to use Typst for creating presentations and documents in this course, including installation, configuration, and practical examples.

## What is Typst?

Typst is a modern markup-based typesetting system designed to be an alternative to LaTeX. It offers:

- **⚡ Fast compilation** (seconds vs minutes)
- **🔧 Better error messages** (clear and helpful)
- **📝 Clean syntax** (more readable than LaTeX)
- **🔄 Single-pass compilation** (no need to run multiple times)
- **🎨 Modern features** (built-in scripting, better graphics)

## Installation on Linux

### Method 1: Download Binary (Recommended)

```bash
# Download latest release
wget -O typst.tar.xz "https://github.com/typst/typst/releases/latest/download/typst-x86_64-unknown-linux-musl.tar.xz"

# Extract and install to local bin
tar -xf typst.tar.xz
mkdir -p ~/.local/bin
mv typst-x86_64-unknown-linux-musl/typst ~/.local/bin/

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Clean up
rm -rf typst.tar.xz typst-x86_64-unknown-linux-musl

# Verify installation
typst --version
```

### Method 2: Using Package Managers

```bash
# Ubuntu/Debian (if available)
sudo apt install typst

# Arch Linux
sudo pacman -S typst

# Using cargo (Rust package manager)
cargo install --locked typst-cli
```

### Method 3: Using Snap

```bash
sudo snap install typst
```

## Basic Typst Syntax

### Document Structure

```typst
// Document metadata
#set document(
  title: "Your Document Title",
  author: "Your Name"
)

// Page configuration
#set page(
  width: 16cm,
  height: 9cm,
  margin: (x: 1.5cm, y: 1cm)
)

// Text formatting
#set text(
  font: "Liberation Sans",
  size: 12pt
)

// Your content goes here
= Main Heading
== Subheading
=== Sub-subheading

Regular text with *bold* and _italic_ formatting.
```

### Mathematical Notation

```typst
// Inline math
The equation is $x^2 + y^2 = z^2$.

// Display math
$ integral_0^infinity e^(-x^2) dif x = sqrt(pi)/2 $

// Complex expressions
$ sum_(i=1)^n x_i = (n(n+1))/2 $

// Matrices
$ mat(1, 2; 3, 4) $

// Bold vectors
$ bold(v) = (x, y, z) $
```

### Lists and Structure

```typst
// Unordered lists
- First item
- Second item
  - Nested item
  - Another nested item

// Ordered lists
1. First step
2. Second step
3. Third step

// Definition lists
/ Term: Definition of the term
/ Another term: Another definition
```

### Tables

```typst
#table(
  columns: 3,
  stroke: 0.5pt,
  [*Header 1*], [*Header 2*], [*Header 3*],
  [Row 1, Col 1], [Row 1, Col 2], [Row 1, Col 3],
  [Row 2, Col 1], [Row 2, Col 2], [Row 2, Col 3]
)
```

## Presentation-Specific Features

### Slide Function (Custom)

```typst
// Define slide function
#let slide(title: none, content) = {
  pagebreak(weak: true)
  if title != none [
    #set text(size: 18pt, weight: "bold")
    #title
    #v(0.8cm)
  ]
  content
}

// Use slides
#slide(title: [Introduction])[
  - Point one
  - Point two
  - Point three
]

#slide(title: [Mathematical Content])[
  The quadratic formula is:
  $ x = (-b plus.minus sqrt(b^2 - 4a c))/(2a) $
]
```

### Section Slides

```typst
// Section slide function
#let section-slide(title) = {
  pagebreak(weak: true)
  set text(size: 20pt, weight: "bold")
  align(center + horizon)[#title]
}

// Usage
#section-slide[Chapter 1: Introduction]
```

## Working with the Course Presentations

### Compiling Presentations

```bash
# Navigate to the beamer directory
cd lessons/4_Factor_Analysis/beamer

# Compile the presentation
typst compile factor_analysis_presentation.typ

# Watch for changes and auto-compile
typst watch factor_analysis_presentation.typ

# Compile to a specific output file
typst compile factor_analysis_presentation.typ output.pdf
```

### Live Development Workflow

```bash
# Terminal 1: Watch and auto-compile
cd lessons/4_Factor_Analysis/beamer
typst watch factor_analysis_presentation.typ

# Terminal 2: Open PDF viewer (updates automatically)
evince factor_analysis_presentation.pdf &

# Or use a web browser for auto-refresh
firefox factor_analysis_presentation.pdf &
```

## VS Code Integration (Recommended)

### Install Extensions

1. **Typst LSP** - Language server support
2. **Typst Preview** - Live preview in VS Code

### VS Code Settings

Add to your `settings.json`:

```json
{
  "typst-lsp.exportPdf": "onSave",
  "typst-preview.refresh": "onSave",
  "files.associations": {
    "*.typ": "typst"
  }
}
```

### Keybindings

Add to your `keybindings.json`:

```json
[
  {
    "key": "ctrl+shift+p",
    "command": "typst-preview.preview",
    "when": "resourceExtname == .typ"
  }
]
```

## Common Patterns for Course Materials

### Title Slide Template

```typst
#align(center)[
  #v(2cm)
  #text(size: 24pt, weight: "bold")[Course Title]
  #v(0.5cm)
  #text(size: 16pt)[Your Name]
  #v(0.3cm)
  #text(size: 14pt)[Institution]
  #v(0.3cm)
  #text(size: 12pt)[#datetime.today().display()]
]
```

### Code Blocks

```typst
// Python code example
```python
import numpy as np
from sklearn.decomposition import PCA

# Create PCA object
pca = PCA(n_components=2)
pca.fit(data)
```

### Including Images

```typst
// Include an image
#figure(
  image("path/to/image.png", width: 80%),
  caption: [Figure caption here]
)

// Image with specific dimensions
#image("plots/scree_plot.png", width: 12cm, height: 8cm)
```

### Cross-references

```typst
// Label an equation
$ E = m c^2 $ <einstein>

// Reference it later
As shown in @einstein, energy and mass are equivalent.

// Label a figure
#figure(
  image("plot.png"),
  caption: [Important plot]
) <important-plot>

// Reference the figure
See @important-plot for details.
```

## Advanced Features

### Custom Functions

```typst
// Define a highlight function
#let highlight(content) = {
  rect(
    fill: yellow.lighten(80%),
    inset: 0.3em,
    radius: 0.2em,
    content
  )
}

// Use it
#highlight[Important concept to remember!]
```

### Conditional Content

```typst
// Show content only in certain conditions
#let show-solutions = true

#if show-solutions [
  *Solution:* The answer is 42.
]
```

### Loops and Data

```typst
// Generate content programmatically
#let data = (
  ("Item 1", "Description 1"),
  ("Item 2", "Description 2"),
  ("Item 3", "Description 3")
)

#for (item, desc) in data [
  - *#item*: #desc
]
```

## File Organization Best Practices

### Recommended Structure

```
lessons/
├── TYPST_GUIDE.md                    # This guide
├── 4_Factor_Analysis/
│   ├── beamer/
│   │   ├── factor_analysis_presentation.typ  # Main presentation
│   │   ├── factor_analysis_presentation.pdf  # Generated PDF
│   │   ├── README.md                          # Specific documentation
│   │   ├── legacy_latex/                      # Legacy LaTeX files
│   │   └── old_artifacts/                     # Build artifacts
│   └── code/                                  # Code examples
└── shared/
    ├── templates/                             # Reusable templates
    └── assets/                                # Shared images, etc.
```

### Template Files

Create reusable templates:

```typst
// templates/course_presentation.typ
#let course-slide(title: none, content) = {
  // Standard slide formatting
}

#let course-title(title, author, date) = {
  // Standard title slide
}

// Import in your presentations
#import "../shared/templates/course_presentation.typ": *
```

## Troubleshooting

### Common Issues

1. **Font not found**: Use system fonts like "Liberation Sans" or "DejaVu Sans"
2. **Math symbols**: Use `$` for inline and `$ ... $` for display math
3. **Images not loading**: Check file paths are relative to the `.typ` file
4. **Compilation errors**: Typst provides clear error messages with line numbers

### Performance Tips

- Use `typst watch` for development (auto-recompile on changes)
- Keep images reasonably sized (< 5MB each)
- Use vector formats (SVG, PDF) when possible
- Cache compiled results with `--cache-dir` flag

### Getting Help

- **Official Documentation**: https://typst.app/docs/
- **Community Forum**: https://forum.typst.app/
- **GitHub Issues**: https://github.com/typst/typst/issues
- **Examples Repository**: https://github.com/typst/typst/tree/main/tests

## Migrating from LaTeX

### Syntax Comparison

| LaTeX | Typst | Description |
|-------|--------|-------------|
| `\textbf{text}` | `*text*` | Bold text |
| `\textit{text}` | `_text_` | Italic text |
| `\section{Title}` | `= Title` | Section heading |
| `\begin{itemize}` | `-` (dash) | Unordered list |
| `\begin{enumerate}` | `1.` (number) | Ordered list |
| `\usepackage{package}` | `#import "@preview/package"` | Import packages |
| `$$math$$` | `$ math $` | Display math |
| `$math$` | `$math$` | Inline math |

### Migration Workflow

1. **Start with structure**: Convert headings and basic formatting
2. **Handle math**: Most LaTeX math works with minor changes
3. **Convert lists and tables**: Use Typst's simpler syntax
4. **Test frequently**: Compile often to catch issues early
5. **Keep LaTeX as reference**: Preserve original files during migration

## Course-Specific Examples

### Factor Analysis Presentation

The current Factor Analysis presentation demonstrates:

- Mathematical notation for PCA and Factor Analysis
- Multi-part document structure
- Clean slide layouts
- Table of contents generation
- Section organization

Study `lessons/4_Factor_Analysis/beamer/factor_analysis_presentation.typ` for a complete example.

### Creating New Presentations

1. Copy the template structure from existing presentations
2. Update metadata (title, author, date)
3. Modify content sections as needed
4. Compile and iterate

### Performance Benefits Achieved

- **Compilation time**: LaTeX 9.4s → Typst 0.2s (47x faster)
- **File size**: Similar quality, often smaller
- **Error debugging**: Much clearer error messages
- **Maintenance**: Easier to edit and modify

---

## Quick Reference Card

### Essential Commands
```bash
typst compile file.typ          # Compile once
typst watch file.typ           # Auto-compile on changes
typst compile file.typ out.pdf # Specify output name
typst --help                   # Show all options
```

### Key Syntax
```typst
= Heading 1              // Section
== Heading 2             // Subsection  
*bold* _italic_          // Formatting
$x^2$                    // Inline math
$ x^2 $                  // Display math
- item                   // List item
#function(args)          // Function call
// comment               // Comment
```

This guide should get you started with Typst for course development. The system is designed to be intuitive, so don't hesitate to experiment!