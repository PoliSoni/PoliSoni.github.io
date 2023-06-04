---
title: "An interactive graph"
description: "Creating an interactive graph with NetworkX and PyVis"
pubDate: "June 5 2023"
heroImage: "https://d3-graph-gallery.com/img/block/block_networkMiserable.png"
---
## How to create an intercative graph?

Intercativity is crucial, particularly when you have lots of data and information to show to your audience. In our project, we aim to show how different political candidates are related to one another, for example their party affiliations, locations, religions and so much more. 

To create an interactive graph, we can make use of NetworkX to create static network graphs and use PyVis to convert the graph into an interactive graph

## Code snippet

Using NetworkX and PyVis in Python, we can create the graph.
```python
from pyvis.network import Network
import networkx as nx

G = nx.Graph() #create graph object

G.add_nodes_from(["Politician_1","Politician_2","Politician_3"]) #create nodes
G.add_edges_from([("Politician_1","Politician_2"),("Politician_3","Politician_1")]) #create edges 

nt = Network('750px', '500px', notebook=True) #create a PyVis network graph of 500px * 500px

nt.from_nx(G) #converting to a PyVis object 
nt.show('nx.html') #save as html
```
<!-- Interactive graph below-->
### Simple undirected graph
<html>
    <head>
        <meta charset="utf-8">
            <script src="lib/bindings/utils.js"></script>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/dist/dist/vis-network.min.css" integrity="sha512-WgxfT5LWjfszlPHXRmBWHkV2eceiWTOBvrKCNbdgDYTHrT2AeLCGbF4sZlZw3UMN3WtL0tGUoIAKsu8mllg/XA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/dist/vis-network.min.js" integrity="sha512-LnvoEWDFrqGHlHmDD2101OrLcbsfkrzoSpvtSQtxK3RMnRV0eOkhhBN2dXHKRrUU8p2DGRTk35n4O8nWSVe1mQ==" crossorigin="anonymous" referrerpolicy="no-referrer">
            </script>
        <center>
          <h1></h1>
        </center>
        <style type="text/css">
             #mynetwork {
                 width: 750px;
                 height: 500px;
                 background-color: #ffffff;
                 border: 1px solid lightgray;
                 position: relative;
                 float: left;
             }    
        </style>
    </head>
    <body>
        <div class="card" style="width: 100%">
            <div id="mynetwork" class="card-body"></div>
        </div>
        <script type="text/javascript">
              // initialize global variables.
              var edges;
              var nodes;
              var allNodes;
              var allEdges;
              var nodeColors;
              var originalNodes;
              var network;
              var container;
              var options, data;
              var filter = {
                  item : '',
                  property : '',
                  value : []
              };
              // This method is responsible for drawing the graph, returns the drawn network
              function drawGraph() {
                  var container = document.getElementById('mynetwork');
                  // parsing and collecting nodes and edges from the python
                  nodes = new vis.DataSet([{"color": "#97c2fc", "id": "Politician_1", "label": "Politician_1", "shape": "dot", "size": 10}, {"color": "#97c2fc", "id": "Politician_2", "label": "Politician_2", "shape": "dot", "size": 10}, {"color": "#97c2fc", "id": "Politician_3", "label": "Politician_3", "shape": "dot", "size": 10}]);
                  edges = new vis.DataSet([{"from": "Politician_1", "to": "Politician_2", "width": 1}, {"from": "Politician_1", "to": "Politician_3", "width": 1}]);
                  nodeColors = {};
                  allNodes = nodes.get({ returnType: "Object" });
                  for (nodeId in allNodes) {
                    nodeColors[nodeId] = allNodes[nodeId].color;
                  }
                  allEdges = edges.get({ returnType: "Object" });
                  // adding nodes and edges to the graph
                  data = {nodes: nodes, edges: edges};
                  var options = {
    "configure": {
        "enabled": false
    },
    "edges": {
        "color": {
            "inherit": true
        },
        "smooth": {
            "enabled": true,
            "type": "dynamic"
        }
    },
    "interaction": {
        "dragNodes": true,
        "hideEdgesOnDrag": false,
        "hideNodesOnDrag": false
    },
    "physics": {
        "enabled": true,
        "stabilization": {
            "enabled": true,
            "fit": true,
            "iterations": 1000,
            "onlyDynamicEdges": false,
            "updateInterval": 50
        }
    }
};
                network = new vis.Network(container, data, options);
                return network;
                }
              drawGraph();
        </script>
    </body>
</html>
