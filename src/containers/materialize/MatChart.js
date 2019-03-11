import React from 'react';
import axios from 'axios';
import * as constants from '../../constants';

import NumberHighlight from '../../components/NumberHighlight';
import VendorTreeMap from '../../components/data-visualisation/TreeMap';
import BoxPlot from '../../components/data-visualisation/BoxPlot';

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
        this.setState({ numbers: [{ title: "First", number: 10, content: "Blabla" }, { title: "Second", number: 20, content: "Blabla" }, { title: "Third", number: 30, content: "Blabla" }] });
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
    console.dir(data);
    // return (
    // <div {...props}>
    //     {data.map((treemap, id) => {
    return (
        <VendorTreeMap
            {...props}
            // key={"tr-" + id}
            width="1000"
            height="500"
            data={data} />);
    //     })}
    // </div>
    // );
}

const MatBoxPlotListView = ({ data, ...props }) => {
    const boxPlotData = [{}];
    return (
        <div {...props}>
            <BoxPlot data={boxPlotData} />
        </div>
    );
}


export { MatNumberHighlightListView, MatChart };