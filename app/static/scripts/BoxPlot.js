import React from 'react';
import { VictoryBoxPlot } from 'victory';

class BoxPlot extends React.Component {
  render() {
    console.log("Here comes the render!")
    return (
      <div>
        <VictoryBoxPlot
          minLabels
          maxLabels
          data={[
            { x: 1, y: [1, 2, 3, 5] },
            { x: 2, y: [3, 2, 8, 10] },
            { x: 3, y: [2, 8, 6, 5] },
            { x: 4, y: [1, 3, 2, 9] }
          ]}
          style={{
            min: { stroke: "tomato" },
            max: { stroke: "orange" },
            q1: { fill: "tomato" },
            q3: { fill: "orange" },
            median: { stroke: "white", strokeWidth: 2 },
            minLabels: { fill: "tomato" },
            maxLabels: { fill: "orange" }
          }}
          />
      </div>
    );
  }}
export default BoxPlot;
