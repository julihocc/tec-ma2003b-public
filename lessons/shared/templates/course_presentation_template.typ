// Course Presentation Template for MA2003B
// Copy this file and modify for your own presentations

// Page and document configuration
#set page(
  width: 16cm,
  height: 9cm,
  margin: (x: 1.5cm, y: 1cm),
  numbering: "1"
)

#set document(
  title: "Your Presentation Title",
  author: "Dr. Juliho Castillo"
)

#set text(
  font: "Liberation Sans",
  size: 12pt,
  lang: "es"
)
#set math.equation(numbering: none)

// Custom slide function
#let slide(title: none, content) = {
  pagebreak(weak: true)
  if title != none [
    #set text(size: 18pt, weight: "bold")
    #title
    #v(0.8cm)
  ]
  content
}

// Section slide function
#let section-slide(title) = {
  pagebreak(weak: true)
  set text(size: 20pt, weight: "bold")
  align(center + horizon)[#title]
}

// ===========================================================================
// TITLE SLIDE
// ===========================================================================

#align(center)[
  #v(2cm)
  #text(size: 24pt, weight: "bold")[Your Presentation Title]
  #v(0.5cm)
  #text(size: 18pt)[Chapter X: Topic Name]
  #v(0.5cm)
  #text(size: 16pt)[Dr. Juliho Castillo]
  #v(0.3cm)
  #text(size: 14pt)[Tecnológico de Monterrey]
  #v(0.3cm)
  #text(size: 12pt)[MA2003B - Análisis Multivariado]
  #v(0.3cm)
  #text(size: 12pt)[#datetime.today().display()]
]

// ===========================================================================
// TABLE OF CONTENTS
// ===========================================================================

#slide(title: [Contenido])[
  #outline(depth: 2)
]

// ===========================================================================
// SECTION 1: INTRODUCTION
// ===========================================================================

#section-slide[Introducción]

#slide(title: [Overview])[
  - Point one with *emphasis*
  - Point two with _italics_
  - Point three with regular text
    - Nested point A
    - Nested point B
]

#slide(title: [Mathematical Content Example])[
  Basic inline math: The equation is $x^2 + y^2 = z^2$.
  
  Display math:
  $ integral_0^infinity e^(-x^2) dif x = sqrt(pi)/2 $
  
  Complex expressions:
  $ sum_(i=1)^n x_i = (n(n+1))/2 $
]

// ===========================================================================
// SECTION 2: MAIN CONTENT
// ===========================================================================

#section-slide[Contenido Principal]

#slide(title: [Data Analysis Example])[
  Steps in the analysis:
  
  1. Data preparation and cleaning
  2. Exploratory data analysis
  3. Model fitting and validation
  4. Results interpretation
]

#slide(title: [Results Summary])[
  Key findings from the analysis:
  
  - Finding 1: Statistical significance achieved
  - Finding 2: Model explains 85% of variance
  - Finding 3: Assumptions validated
  
  *Conclusion*: The method works well for this application.
]

// ===========================================================================
// SECTION 3: CONCLUSION
// ===========================================================================

#section-slide[Conclusiones]

#slide(title: [Key Takeaways])[
  - Important finding #1
  - Critical insight #2  
  - Practical implication #3
  
  #v(0.5cm)
  
  #align(center)[
    #rect(
      fill: blue.lighten(90%),
      stroke: blue.lighten(60%),
      inset: 0.5em,
      radius: 0.3em,
      [*Main conclusion*: Your key message goes here.]
    )
  ]
]

#slide(title: [Template Usage])[
  *To use this template:*
  
  1. Copy this file to your presentation directory
  2. Rename to your presentation name
  3. Update the title slide information
  4. Replace content sections with your material
  5. Compile with: `typst compile my_presentation.typ`
  
  *Available functions:*
  - `#slide(title: [Title])[content]` - Regular slide
  - `#section-slide[Title]` - Section divider
]