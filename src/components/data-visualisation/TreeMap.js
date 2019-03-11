import React from 'react';
import * as d3 from 'd3';

const VendorTreeMap = ({ data, width, height }) => {
    const drawTreemap = (data) => {
        let root = d3.hierarchy(data);
        let treemap = d3.treemap()
            .size([width, height])
            .padding(4)
            .paddingOuter(10);
        root
            .sum(d => d.size) // Creates the values of each node
            .sort((a, b) => b.size - a.size); // Creates the hierarchy between each node
        treemap(root);
        return root.descendants().map((d, id) => <Leaf key={'leaf' + id} d={d} />);
    }

    return (
        <svg
            viewBox={`0,0,${width},${height}`}
            style={{ width: '100%', height: 'auto', font: '20px sans-serif' }}
            className="treemap-container"
            width={width}
            height={height}
        >
            {data && drawTreemap(data)}
        </svg>
    );
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

export default VendorTreeMap;