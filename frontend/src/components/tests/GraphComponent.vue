<template>
  <div style="border:solid 1px black; width:400px; height:400px;"></div>
</template>


<script>
  import go from 'gojs';

  var $ = go.GraphObject.make;  // for conciseness

  export default {
      mounted: function() {
        var diagram =
        $(go.Diagram, this.$el, {
            "undoManager.isEnabled": true,
            "grid.gridCellSize": new go.Size(30, 30),
        });

      // define a simple Node template
        diagram.nodeTemplate =
          $(go.Node, "Auto",  // the Shape will go around the TextBlock
            $(go.Shape, "RoundedRectangle",
              // Shape.fill is bound to Node.data.color
              new go.Binding("fill", "color")),
            $(go.TextBlock,
              { margin: 3 },  // some room around the text
              // TextBlock.text is bound to Node.data.key
            new go.Binding("text", "key"))
        );
        diagram.model = new go.GraphLinksModel(
        [
          { key: "Alpha", color: "lightblue" },
          { key: "Beta", color: "orange" },
          { key: "Gamma", color: "lightgreen" },
          { key: "Delta", color: "pink" }
        ],
        [
          { from: "Alpha", to: "Beta" },
          { from: "Alpha", to: "Gamma" },
          { from: "Beta", to: "Beta" },
          { from: "Gamma", to: "Delta" },
          { from: "Delta", to: "Alpha" }
        ]);
      }
  }
</script>
