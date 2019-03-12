import React from 'react';
import axios from 'axios';
import * as constants from '../../constants';

import NumberHighlight from '../../components/NumberHighlight';
import VendorTreeMap from '../../components/data-visualisation/TreeMap';
// import DynamicTreemapExample from '../../components/data-visualisation/CustomTreeMap';
import BoxPlotChart from '../../components/data-visualisation/BoxPlot';

class MatChart extends React.Component {
    state = {
        numbers: [],
        treemaps: [],
        boxplot: []
    }

    componentDidMount() {
        // axios.get(constants.NUMBERS_URL)
        //     .then(res => {
        //         this.setState({ numbers: res.data });
        //     });
        axios.get(constants.TREEMAP_URL)
            .then(res => {
                this.setState({ treemaps: res.data });
            });
        // axios.get(constants.BOXPLOT_URL)
        //     .then(res => {
        //         this.setState({ boxplot: res.data });
        //     });
        this.setState({ numbers: [{ title: "Number of referenced cars", number: 100, content: "Evolution through time" }, { title: "Number of retailer scraped", number: 3, content: "Trend" }, { title: "Average price of a car", number: 300, content: "Blabla" }] });
        // this.setState({ treemaps: [{}] });
        this.setState({ boxplot: [{}] });
    }

    render() {
        const { numbers, treemaps, boxplot } = this.state;
        return (
            <>
                <h2 className="center-align row">Charts</h2>
                <MatNumberHighlightListView data={numbers} className="row" />
                <MatTreemapListView data={treemaps} className="row" />
                <MatBoxPlotListView data={boxplot} className="row" />
            </>
        );
    }
}

const MatNumberHighlightListView = ({ data, ...props }) => {
    const colWidth = Math.floor(12 / data.length);
    return (
        <div {...props}>
            {data.map((hl, i) => <NumberHighlight data={hl} layoutClass={"col m" + colWidth} key={"num-" + i} />)}
        </div>
    );
}

const MatTreemapListView = ({ data = [], ...props }) => {
    return (
        <VendorTreeMap
            {...props}
            width="1000"
            height="500"
            data={data} />
        // <DynamicTreemapExample />
    );
}

const MatBoxPlotListView = ({ data, ...props }) => {
    const boxPlotData = [{ key: 'Volvo', values: [{ key: "Volvo", value: 1000 }, { key: "Volvo", value: 2040 }, { key: "Volvo", value: 2300 }, { key: "Volvo", value: 8000 }] }, { key: 'Mercedes', values: [{ key: "Volvo", value: 1000 }, { key: "Volvo", value: 2040 }, { key: "Volvo", value: 2300 }, { key: "Volvo", value: 8000 }] }, { key: 'CLicli', values: [{ key: "Volvo", value: 1000 }, { key: "Volvo", value: 2040 }, { key: "Volvo", value: 2300 }, { key: "Volvo", value: 8000 }] }]
    return (
        <div {...props}>
            <BoxPlotChart width='800' height='800' data={boxPlotData} />
        </div>
    );
}


export { MatNumberHighlightListView, MatChart };