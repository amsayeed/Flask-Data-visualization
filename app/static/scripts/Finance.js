import React from 'react';
import {
	VictoryBar,
	VictoryChart,
	VictoryLabel,
	VictoryAxis,
	VictoryTheme,
	VictoryStack
} from "victory";

class Finance extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
		error: null,
		isLoaded: false,
		items: {}
		};
	}
	
	componentDidMount() {
		let url = window.location.href.replace(/.*finance/).split("/");
		console.log(url[1] + " " + url[2]);
		const company_id = url[1];
		const year = url[2];
		const api_url = "/api_1_0/get_finances/" + company_id + "/" + year;
		fetch(api_url)
		.then(res => res.json())
		.then(
			(result) => {
				const { status, message } = result
				// console.log(error)
				console.log(result)
				console.log(status)
				console.log(message)
			this.setState({
				isLoaded: true,
				items: result.content
			});
			},
			(error) => {
			this.setState({
				isLoaded: true,
				error
			});
			}
		)
	}

	make_chart_data(items) {
		let my_data_list = [];
		my_data_list.push(0)
		my_data_list.push(items.q1_earnings)
		my_data_list.push(items.q2_earnings)
		my_data_list.push(items.q3_earnings)
		my_data_list.push(items.q4_earnings)
		// console.log(items.q1_earnings)
		// console.log(items.q2_earnings)
		// console.log(items.q3_earnings)
		// console.log(items.q4_earnings)
		// console.log(items.year)

		return my_data_list;
	}

	render() {
		console.log(this.state)
		const { error, isLoaded, items } = this.state;

		// // const finance_axis = this.make_chart_axis(items);
		const finance_data = this.make_chart_data(items);
		const finance_axis = ["Q1", "Q2", "Q3", "Q4"];
		// const finance_axis = [1, 2, 3, 4];
		console.log(finance_axis)
		console.log(finance_data)
		if (error) {
			// return <div>Error: {error.message}</div>;
			return <div>Error loading data.</div>;
		} else if (!isLoaded) {
		return <div>Loading...</div>;
		} else {
		return (


			<section className="victory-chart-wrapper">
				<div className="finance-chart">
					<h2>Company Finances:</h2>

					<VictoryChart
						padding={{ left: 100, right: 50, bottom: 100, top: 30 }}
						fontSize={8}
						// style={{ parent: { height: "25%", width: "70%" } }}
						domainPadding={20}
						theme={VictoryTheme.material}
					>
						<VictoryAxis tickValues={finance_axis} />
						<VictoryAxis dependentAxis tickFormat={x => `$${x/1000000} M`} />


						<VictoryStack colorScale={"warm"}>
							<VictoryBar
								data={finance_data}
							/>
						</VictoryStack>
					</VictoryChart>


				</div>
			</section>


		);
		}
	}
}
export default Finance;
