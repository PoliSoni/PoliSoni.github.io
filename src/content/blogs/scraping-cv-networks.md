---
title: "Scraping CV networks"
description: "A simple explanation of our infrastructure to scrape CV content on a digital database"
pubDate: "May 16 2023"
heroImage: "https://w0.peakpx.com/wallpaper/581/454/HD-wallpaper-network-concept-darkness-points-and-lines-social-network-abstract-art-network.jpg"
---

<!-- Config mathjax -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS_HTML"></script>

### Basics of network
A graph is defined as 

$$
\{G = (V,E)}\
$$

where V is the vertice (i.e., node) and E is the edge (i.e., connection between nodes).  

In simple undirected graph, the degree of a node is the total edges incidenting V<sub>i</sub>:

$$
\{Deg(v) = |{u: (u, v) \in E|}}\
$$
where <strong>u</strong> denotes all nodes in the graph. 

Using python, we can compute the degree as follow:

```python
# Calcuating degree
degree = 0
for edge in graph: #for each pairs in a graph (a list)
    if node in edge: #check if a certain node exist in this pair
        degree += 1 #is yes, degree + 1
```
