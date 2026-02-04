#set page(
  paper: "a4",
  margin: (x: 1.25in, y: 1.25in),
)

#set text(
  font: "New Computer Modern",
  size: 11pt,
)

#align(center)[
  #text(size: 2em, weight: "bold")[Lab Report: Graph algorithms]

  #v(1em)

  #text(size: 1.5em)[2XC3 Lab 2]

  #v(1em)

  #text(size: 1.2em)[Marko Kosoric, Patrick Chen]

  #v(1em)

  #text(size: 1em)[February 22, 2026]
]

#pagebreak()

#outline()

#outline(title: "Figures", target: figure.where(kind: image))

#pagebreak()

#show figure.where(
  kind: image,
): set figure.caption(position: top)
