import React from 'react';
import axios from 'axios';
import * as constants from '../../constants';
import { getColor } from '../../utils';

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
        axios.get(constants.NUMBERS_URL)
            .then(res => {
                this.setState({ numbers: res.data });
            });
        axios.get(constants.TREEMAP_URL)
            .then(res => {
                this.setState({ treemaps: res.data });
            });
        axios.get(constants.BOXPLOT_URL)
            .then(res => {
                this.setState(
                    { boxplot: res.data.sort((a, b) => b.values.length - a.values.length).splice(0, 10) }
                );
            });
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
    const colorFn = getColor(data.length);
    return (
        <div {...props}>
            {data.map((hl, i) => <NumberHighlight data={hl} layoutClass={"col m" + colWidth} color={colorFn()} key={"num-" + i} />)}
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
    // const bins = data.sort((a, b) => b.values.length - a.values.length).splice(0, 10);
    return (
        <BoxPlotChart ratio="95%" data={data} {...props} />
    );
}

export { MatNumberHighlightListView, MatChart };