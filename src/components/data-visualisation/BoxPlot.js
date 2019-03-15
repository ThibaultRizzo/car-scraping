import React from 'react';
// import PropTypes from 'prop-types';
import Axis from './Axis';
import * as d3 from 'd3';

const BoxPlotChart = ({ ratio, data = [] }) => {
    let width = 300;
    let height = 300;
    let maxValue = 100000;
    return (
        <svg
            viewBox={`0,0,1100,400`}
            // style={{ width: '100%', height: 'auto', font: '20px sans-serif' }}
            className="boxplotchart"
            width={ratio}
            height="100%"
        >
            {data.length > 0 && <BoxPlot
                x={50}
                y={50}
                step={100}
                width={width}
                height={height}
                data={data}
                maxValue={maxValue}
                datapoint={({ x, y, key }) => <Box x={x} y={y} key={key} width={300} maxValue={maxValue} boxWidth={10} />}
            />}
        </svg>
    );
}

class BoxPlot extends React.PureComponent {
    coordinatesArray = [''].concat(this.props.data.map(val => val.key));
    state = {
        xScale: d3
            .scaleOrdinal()
            .domain(this.coordinatesArray)
            .range(this.coordinatesArray.map((_, index) => index * this.props.step)),
        yScale: d3
            .scaleLinear()
            .domain([0, this.props.maxValue])
            .range([this.props.height, 0])
    };

    static getDerivedStateFromProps(props, state) {
        const { yScale, xScale } = state;

        return {
            ...state,
            yScale,
            xScale
        };
    }

    render() {
        const { x, y, data, height, datapoint } = this.props,
            { yScale, xScale } = this.state;
        return (
            <g transform={`translate(${x}, ${y})`}>
                {data.map(({ key, values }, index) => datapoint({ x: xScale(key), y: values.map(el => yScale(el.price)), key: 'data' + index }))}
                <Axis x={0} y={0} scale={yScale} type="Left" />
                <Axis x={0} y={height} scale={xScale} type="Bottom" />
            </g>
        );
    }
}

class Box extends React.Component {
    state = {
        hovered: false
    };

    computePlotData = (bin) => {
        let binMeta = {};
        const values = bin.sort((a, b) => a - b);
        const min = values[0];
        const max = values[values.length - 1];
        const q1 = d3.quantile(values, 0.25);
        const q2 = d3.quantile(values, 0.50);
        const q3 = d3.quantile(values, 0.75);
        const iqr = q3 - q1; // interquartile range
        const r0 = Math.max(min, q1 - iqr * 1.5);
        const r1 = Math.min(max, q3 + iqr * 1.5);
        binMeta.quartiles = [q1, q2, q3];
        binMeta.range = [r0, r1];
        binMeta.outliers = bin.filter(v => v < r0 || v > r1); // TODO
        return binMeta;
    }

    normalizeData = (d) => Math.floor((this.props.width - d) * this.props.maxValue / this.props.width, 1);

    highlight = () => {
        this.setState({ hovered: true });
    };

    unhighlight = () => {
        this.setState({ hovered: false });
    };


    render() {
        const lineStyle = { opacity: 1 };
        const recStyle = this.state.hovered
            ? { fill: '#72bfff', opacity: 0.8 }
            : { fill: 'steelblue', opacity: 0.8, transition: '0.5s' };
        const { quartiles, range } = this.computePlotData(this.props.y);
        const { x, boxWidth } = this.props;
        return (
            <g onMouseOver={this.highlight} onMouseOut={this.unhighlight}
                transform={`translate(${x - boxWidth / 2},0)`} style={{ stroke: 'black', strokeWidth: '1px' }}>
                <line className="center" x1={boxWidth / 2} y1={range[1]} x2={boxWidth / 2} y2={range[0]} style={lineStyle}></line>
                <rect className="box" x="0" y={quartiles[0]} width={boxWidth} height={quartiles[2] - quartiles[0]} style={recStyle}></rect>
                <line className="median" x1="0" y1={quartiles[2]} x2={boxWidth} y2={quartiles[2]}></line>
                <line className="whisker" x1="0" y1={range[1]} x2={boxWidth} y2={range[1]} style={lineStyle}></line>
                <line className="whisker" x1="0" y1={range[0]} x2={boxWidth} y2={range[0]} style={lineStyle}></line>
                {/* TODO: Add outliers */}
                {/* <circle className="outlier" r=" 5" cx="27" cy="0" style={lineStyle}></circle> */}
                {this.state.hovered &&
                    <>
                        <text className="box" dy=".1em" dx="-6" x="0" y={quartiles[0]} textAnchor="end">{this.normalizeData(quartiles[0])}</text>
                        <text className="box" dy=".3em" dx="6" x={boxWidth} y={quartiles[1]} textAnchor="start">{this.normalizeData(quartiles[1])}</text>
                        <text className="box" dy=".3em" dx="-6" x="0" y={quartiles[2]} textAnchor="end">{this.normalizeData(quartiles[2])}</text>
                        <text className="whisker" dy=".3em" dx="6" x={boxWidth} y={range[1]} style={lineStyle}>{this.normalizeData(range[1])}</text>
                        <text className="whisker" dy=".3em" dx="6" x={boxWidth} y={range[0]} style={lineStyle}>{this.normalizeData(range[0])}</text>
                    </>
                }
            </g>
        );
    }
}

BoxPlotChart.propTypes = {
    // width: PropTypes.number.isRequired,
    // height: PropTypes.number.isRequired,
    // data: PropTypes.object.isRequired,
    // animation: AnimationPropType,
    // height: PropTypes.number.isRequired,
    // mode: PropTypes.string,
    // onLeafClick: PropTypes.func,
    // onLeafMouseOver: PropTypes.func,
    // onLeafMouseOut: PropTypes.func,
    // scales: PropTypes.object.isRequired,
    // width: PropTypes.number.isRequired,
    // r: PropTypes.number.isRequired,
    // x0: PropTypes.number.isRequired,
    // x1: PropTypes.number.isRequired,
    // y0: PropTypes.number.isRequired,
    // y1: PropTypes.number.isRequired
};

export default BoxPlotChart;