---
title: "A tree map"
description: "Exploring the activity of parties in each kabupaten"
pubDate: "June 9 2023"
heroImage: public/treemap.png
---
## What is a tree map?

Tree map is a very useful visualisation to show multilevel, hierarchical data. It makes use of sizes of each 'block' on the map to represent values of each level.

## Code snippet
Before visualising the treemap, we must format our data in a hierarchical structure:

| **party name**      | **kabupaten name** | **count** | **Indonesia** |
|---------------------|--------------------|-----------|---------------|
| Demokrat            | ACEH BARAT         | 28        | Indonesia     |
| Demokrat            | ACEH BESAR         | 41        | Indonesia     |
| ...                 | ...                | ...       | ...           |
| Persatuan Indonesia | YALIMO             | 6         | Indonesia     |

Note that we also need a constant variable (i.e., the largest container of the graph) to nest all lower-level variables (i.e., party name and kabupaten). Here our container would be Indonesia.

Using plotly, we can create both static and intercative treemap.
```python
import plotly.express as px

fig = px.treemap(kp_df, path = ['Indonesia','kabupaten_name','party_name'], values = 'count',
                 width=1920,height=1080)

fig.update_traces(hovertemplate='Kabupaten: %{label} <br>Total candidates: %{value}') #customise hover text based on the label and value of the label
fig.show() #show the plot 
```
<!-- Interactive graph below-->
### Tree map

See the tree map [here](/Code/treemap.html)