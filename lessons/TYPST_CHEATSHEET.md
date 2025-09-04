# Typst Quick Reference Cheat Sheet

## Installation & Basic Usage

```bash
# Install (if not already done)
~/.local/bin/typst --version

# Compile once
typst compile presentation.typ

# Watch and auto-compile
typst watch presentation.typ

# Compile with specific output name
typst compile input.typ output.pdf
```

## Essential Syntax

### Text Formatting
```typst
*bold text*
_italic text_
`monospace text`
*_bold and italic_*
```

### Headings
```typst
= Level 1 Heading
== Level 2 Heading  
=== Level 3 Heading
```

### Lists
```typst
// Unordered
- Item 1
- Item 2
  - Nested item

// Ordered
1. First item
2. Second item

// Definition
/ Term: Definition
/ Another: Another definition
```

### Mathematics
```typst
// Inline: $x^2 + y^2 = z^2$
// Display:
$ sum_(i=1)^n x_i = mu $

// Common symbols
$alpha$, $beta$, $gamma$
$sum$, $integral$, $infinity$
$<=, >=, !=, approx$
$bold(x)$, $vec(v)$
```

### Tables
```typst
#table(
  columns: 3,
  [*Col 1*], [*Col 2*], [*Col 3*],
  [Data 1], [Data 2], [Data 3]
)
```

### Code Blocks
```typst
```python
def hello():
    print("Hello, World!")
```
```

### Images
```typst
#image("path/to/image.png", width: 80%)

#figure(
  image("plot.png"),
  caption: [Figure caption]
)
```

### Functions & Variables
```typst
#let my-function(x) = x * 2
#let result = my-function(5)

#if condition [
  Show this content
]

#for item in (1, 2, 3) [
  Item: #item
]
```

## Presentation-Specific

### Slide Template
```typst
#let slide(title: none, content) = {
  pagebreak(weak: true)
  if title != none [
    #set text(size: 18pt, weight: "bold")
    #title
    #v(0.8cm)
  ]
  content
}

// Usage
#slide(title: [My Slide])[
  Slide content goes here
]
```

### Page Setup
```typst
#set page(
  width: 16cm,
  height: 9cm,
  margin: 1.5cm
)

#set text(
  font: "Liberation Sans",
  size: 12pt
)
```

### Common Patterns
```typst
// Center content
#align(center)[Content]

// Add space
#v(1cm)  // vertical
#h(2cm)  // horizontal

// Highlight box
#rect(
  fill: yellow.lighten(80%),
  inset: 0.5em,
  [Important text]
)
```

## VS Code Setup

1. Install "Typst LSP" extension
2. Install "Typst Preview" extension  
3. Open `.typ` file and use Ctrl+Shift+P → "Typst Preview"

## Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| Font not found | Use "Liberation Sans" or system fonts |
| Math not rendering | Use `$math$` for inline, `$ math $` for display |  
| Image not loading | Check file path relative to `.typ` file |
| Function error | Check syntax: `#function()` not `\function{}` |
| Compilation slow | Use `typst watch` for development |

## Migration from LaTeX

| LaTeX | Typst |
|-------|-------|
| `\textbf{bold}` | `*bold*` |
| `\textit{italic}` | `_italic_` |
| `\section{Title}` | `= Title` |
| `\begin{itemize}` | `- item` |
| `\begin{enumerate}` | `1. item` |
| `$$math$$` | `$ math $` |
| `\usepackage{pkg}` | `#import "@preview/pkg"` |

## File Organization

```
lessons/
├── TYPST_GUIDE.md              # Full guide
├── TYPST_CHEATSHEET.md         # This cheat sheet
├── shared/
│   └── templates/
│       └── course_presentation_template.typ
└── 4_Factor_Analysis/
    └── beamer/
        ├── factor_analysis_presentation.typ
        └── factor_analysis_presentation.pdf
```

## Quick Start Workflow

1. Copy template: `cp lessons/shared/templates/course_presentation_template.typ my_presentation.typ`
2. Edit content in VS Code
3. Start watch mode: `typst watch my_presentation.typ`
4. Open PDF in viewer (auto-refreshes)
5. Edit → Save → See changes immediately

---

**📚 For detailed explanations, see `lessons/TYPST_GUIDE.md`**  
**🎯 For templates, see `lessons/shared/templates/`**