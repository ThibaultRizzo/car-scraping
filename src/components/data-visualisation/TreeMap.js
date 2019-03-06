import React from 'react';
import * as d3 from 'd3';
import axios from 'axios';
import PropTypes from 'prop-types';

export default class TreeMap extends React.Component {
    state = {
        data: []
    }
    static propTypes = {
        width: PropTypes.string,
        height: PropTypes.string
    }
    componentWillMount() {
        axios.get(`http://127.0.0.1:8000/car-api/vendors/`)
            .then(res => {
                this.setState({ data: res.data });
            });
    }

    drawTreemap = (data) => {
        let root = d3.hierarchy(data);
        let treemap = d3.treemap()
            .size([this.props.width, this.props.height])
            .padding(4)
            .paddingOuter(10);
        root
            .sum(d => d.size) // Creates the values of each node
            .sort((a, b) => b.size - a.size); // Creates the hierarchy between each node
        treemap(root);
        return root.descendants().map((d, id) => <Leaf key={'leaf' + id} d={d} />);
    }

    render() {
        const { width, height } = this.props;
        return (
            <svg
                viewBox={`0,0,${width},${height}`}
                style={{ width: '100%', height: 'auto', font: '20px sans-serif' }}
                className="treemap-container"
                width={width}
                height={height}
            >
                {this.drawTreemap(this.state.data)}
            </svg>
        );
    }
}


const Leaf = ({ d, key }) => {
    // const getColor = d => { while (d.depth > 1) d = d.parent; return color(d.data.name); }
    // const yText = (d, i, nodes) => `${(i === nodes.length - 1) * 0.3 + 1.1 + i * 0.9}em`;
    // const yOpacity = (d, i, nodes) => i === nodes.length - 1 ? 0.7 : null;
    return (
        <g key={key} transform={`translate(${d.x0},${d.y0})`}>
            {/* <title>`${d.ancestors().reverse().map(d => d.data.name).join("/")}\n${format(d.value)}`</title> */}
            <rect
                // id={`O-leaf-${id}`}
                fill="red"
                fillOpacity="0.6"
                width={d.x1 - d.x0}
                height={d.y1 - d.y0}></rect>
            {/* <clipPath id={`O-leaf-${id}`}>
                <use xlinkHref={d.leafUid.href}>
                </use>
            </clipPath> */}
            <text dx="4" dy="14">
                {/* <tspan x="3" y={yText}>Labeler</tspan>
                <tspan x="3" y="2.3000000000000003em" fill-opacity={yOpacity}>{d}</tspan>
                 */}
                {d.data.name}
            </text>
        </g>
    );
}
