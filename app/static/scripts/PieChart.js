/*global window:false*/
/*eslint-disable no-magic-numbers,react/no-multi-comp*/
import { random, range } from "lodash";
import React from "react";
import { VictoryPie, VictoryTheme, VictoryTooltip } from "victory";
// import { VictoryTooltip } from "../../packages/victory-tooltip/src/index";
// import { VictoryTheme } from "../../packages/victory-core/src/index";

class PieChart2 extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: this.getData(),
      transitionData: this.getTransitionData(),
      colorScale: ["#D85F49", "#F66D3B", "#D92E1D", "#D73C4C", "#FFAF59", "#E28300", "#F6A57F"],
      sliceWidth: 60,
      style: {
        parent: {
          // backgroundColor: "#f7f7f7",
          // border: "1px solid #ccc",
          margin: "2%",
          maxWidth: "100%"
        }
      }
    };
  }

  componentDidMount() {
    /* eslint-disable react/no-did-mount-set-state */
    this.setStateInterval = window.setInterval(() => {
      this.setState({
        data: this.getData(),
        transitionData: this.getTransitionData()
      });
    }, 4000);
  }

  componentWillUnmount() {
    window.clearInterval(this.setStateInterval);
  }

  getTransitionData() {
    const data = random(6, 9);
    return range(data).map((datum) => {
      return {
        x: datum,
        y: random(2, 9),
        label: `#${datum}`
      };
    });
  }

  getData() {
    const rand = () => Math.max(Math.floor(Math.random() * 10000), 1000);
    return [
      { x: "<5", y: rand(), label: "A", fill: "grey" },
      { x: "5-13", y: rand() },
      { x: "14-17", y: rand() },
      { x: "18-24", y: rand() },
      { x: "25-44", y: rand() },
      { x: "45-64", y: rand() },
      { x: "≥65", y: rand() }
    ];
  }

  render() {
    const containerStyle = {
      display: "flex",
      flexDirection: "row",
      flexWrap: "wrap",
      alignItems: "center",
      justifyContent: "center"
    };

    const parentStyle = {
      backgroundColor: "#f7f7f7",
      border: "1px solid #ccc",
      margin: "2%",
      maxWidth: "40%"
    };

    return (
      <div>
        <h1>VictoryPie Demo</h1>

        <div style={containerStyle}>

          <VictoryPie
            style={{ ...this.state.style, labels: { padding: 0 } }}
            data={this.state.data}
            innerRadius={100}
            labelRadius={110}
            animate={{ duration: 2000 }}
            colorScale={this.state.colorScale}
          />

        </div>
      </div>
    );
  }
}
export default PieChart2;
