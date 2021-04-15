console.log("Testing");
//index.js
import React from "react";
import ReactDOM from "react-dom";
import BarChart from "./BarChart";
import BoxPlot from "./BoxPlot";
import PieChart from "./PieChart";
import PieChart2 from "./PieChart2";
import Finance from "./Finance";
import HelloWorld from "./HelloWorld";

console.log("Rendering App")
let url = window.location.href.toLowerCase();
console.log(url)
if (url.includes("finance"))
{
    console.log("Bingpot!")
    ReactDOM.render(<Finance />, document.getElementById("finance-app"));
}
else if (url.includes("chart_examples"))
{
    ReactDOM.render(<BarChart />, document.getElementById("barchart-app"));
    ReactDOM.render(<BoxPlot />, document.getElementById("boxplot-app"));
    ReactDOM.render(<PieChart />, document.getElementById("piechart-app"));
    ReactDOM.render(<PieChart2 />, document.getElementById("piechart2-app"));
}
