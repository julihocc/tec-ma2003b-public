# MA2003B Custom Beamer Theme

A personalized Beamer theme for the MA2003B - Application of Multivariate Methods in Data Science course at Tec de Monterrey.

## Features

- **Tec de Monterrey branding**: Uses official brand colors (blue, gray, green, orange)
- **Clean design**: Based on the modern metropolis theme
- **Course identification**: Automatic MA2003B course code in footer
- **Professional layout**: Suitable for academic presentations
- **Customized blocks**: Color-coded for different content types

## Usage

To use this theme in your presentations, add the following to your LaTeX preamble:

```latex
\documentclass[aspectratio=169]{beamer}
\usetheme{ma2003b}

% Optional: Use the color theme separately
% \usecolortheme{ma2003b}

\title{Your Presentation Title}
\subtitle{Your Subtitle}
\author{Dr. Juliho Castillo}
\institute{Tec de Monterrey}
\date{\today}

\begin{document}
% Your content here
\end{document}
```

## Color Palette

The theme uses the following Tec de Monterrey brand colors:

- **Primary Blue** (`tecblue`): RGB(0, 88, 170) - Used for titles and structure
- **Secondary Gray** (`tecgray`): RGB(102, 102, 102) - Used for subtitles and accents
- **Accent Green** (`tecgreen`): RGB(0, 120, 74) - Used for examples
- **Accent Orange** (`tecorange`): RGB(255, 122, 0) - Used for alerts and progress

## File Structure

- `beamerthemema2003b.sty` - Main theme file
- `beamercolorthemema2003b.sty` - Color theme (can be used independently)
- `README.md` - This documentation

## Installation

The theme files are located in the `beamers/themes/` directory of your MA2003B course repository. LaTeX will automatically find them when compiling presentations from anywhere within the repository structure.

## Customization

You can override specific colors or settings by adding commands after loading the theme:

```latex
\usetheme{ma2003b}

% Override specific colors
\setbeamercolor{frametitle}{bg=red, fg=white}

% Add custom elements
\setbeamertemplate{footline}{} % Remove footer if needed
```

## Examples

All presentations in the course should use this theme for consistency. See existing presentations in the `lesson/` directories for examples.