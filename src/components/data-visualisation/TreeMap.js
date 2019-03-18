import React from 'react';
// import PropTypes from 'prop-types';

import * as d3 from 'd3';
import './TreeMap.scss';

const VendorTreeMap = ({ data, width, height }) => {
    let node, rootNode;
    node = rootNode = data;
    const setTreeColor = (tree, maxValue) => {
        const getColorOfIndex = (index, nbMax = 1) => `hsla(${index * (255 / nbMax)}, 100%, 50%, 1)`;
        if (tree.children) {
            const nbVendors = tree.children.length;
            tree.children.forEach((vendor, index) => {
                let colorDomain = [0, maxValue], colorRange = ['white', getColorOfIndex(index, nbVendors)];
                let colorFn = d3.scaleLinear().range(colorRange).domain(colorDomain);
                vendor.color = colorFn(index);
                setColor(vendor.children, colorFn);
            })
        }
    }
    const setColor = (nodeArray, colorFn) => {
        nodeArray.forEach(node => {
            node.color = colorFn(node.value)
            console.log(node.color);
            if (node.children) {
                setColor(node.children, colorFn);
            }
        });
    }

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
        setTreeColor(root, root.height);
        return root.descendants().map((d, id) =>
            <Leaf root={rootNode} node={node} maxWidth={width} maxHeight={height} max={root.height} colorIndex={id} key={'leaf' + id} d={d} />
        );
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


class Leaf extends React.Component {
    state = {
        hovered: false
    };
    // const yText = (d, i, nodes) => `${(i === nodes.length - 1) * 0.3 + 1.1 + i * 0.9}em`;
    // const yOpacity = (d, i, nodes) => i === nodes.length - 1 ? 0.7 : null;

    // const zoom = (d) => {
    //     var kx = maxWidth / (d.x1 - d.x0), ky = maxHeight / (d.y1 - d.y0);
    //     var x = d3.scaleLinear().range([0, maxWidth])
    //     var y = d3.scaleLinear().range([0, maxHeight])
    //     x.domain([d.x, d.x + d.dx]);
    //     y.domain([d.y, d.y + d.dy]);

    //     // var t = svg.selectAll("g.cell").transition()
    //     //     .duration(d3.event.altKey ? 7500 : 750)
    //     //     .attr("transform", function(d) { return "translate(" + x(d.x) + "," + y(d.y) + ")"; });
    //     debugger;
    //     // t.select("rect")
    //     //     .attr("width", function(d) { return kx * d.dx - 1; })
    //     //     .attr("height", function(d) { return ky * d.dy - 1; })

    //     // t.select("text")
    //     //     .attr("x", function(d) { return kx * d.dx / 2; })
    //     //     .attr("y", function(d) { return ky * d.dy / 2; })
    //     //     .style("opacity", function(d) { return kx * d.dx > d.w ? 1 : 0; });

    //     node = d;
    //     d3.event.stopPropagation();
    // }

    highlight = () => {
        this.setState({ hovered: true });
    };

    unhighlight = () => {
        setTimeout(() => {
            this.setState({ hovered: false });
        }, 500);
    };
    render() {
        const { node, root, d, max, colorIndex, maxWidth, maxHeight, ...props } = this.props;
        return (
            <g transform={`translate(${d.x0},${d.y0})`} {...props} onMouseOver={this.highlight} onMouseOut={this.unhighlight}>
                {/* <title>`${d.ancestors().reverse().map(d => d.data.name).join("/")}\n${format(d.value)}`</title> */}
                <rect
                    // id={`O-leaf-${id}`}
                    fill={d.color}
                    fillOpacity="0.6"
                    width={d.x1 - d.x0}
                    height={d.y1 - d.y0}
                // onClick={d && zoom(node == d.parent ? root : d.parent)}

                ></rect>
                {/* <clipPath id={`O-leaf-${id}`}>
                    <use xlinkHref={d.leafUid.href}>
                    </use>
                </clipPath> */}
                <LeafText isHovered={this.state.hovered} depth={d.depth} maxDepth={3} text={d.data.name} />
            </g>
        );
    }
}

const LeafText = ({ isHovered, depth, maxDepth, text }) => {
    const Text = (
        <text dx="4" dy="14">
            {/* <tspan x="3" y={yText}>Labeler</tspan>
                    <tspan x="3" y="2.3000000000000003em" fill-opacity={yOpacity}>{d}</tspan>
                     */}
            {text}
        </text>
    );
    if (depth < maxDepth && depth > 0) {
        return Text;
    } else if (depth == maxDepth && isHovered) {
        return Text;
    } else {
        return null;
    };
}

// TreemapLeaf.propTypes = {
//     animation: AnimationPropType,
//     height: PropTypes.number.isRequired,
//     mode: PropTypes.string,
//     node: PropTypes.object.isRequired,
//     onLeafClick: PropTypes.func,
//     onLeafMouseOver: PropTypes.func,
//     onLeafMouseOut: PropTypes.func,
//     scales: PropTypes.object.isRequired,
//     width: PropTypes.number.isRequired,
//     r: PropTypes.number.isRequired,
//     x0: PropTypes.number.isRequired,
//     x1: PropTypes.number.isRequired,
//     y0: PropTypes.number.isRequired,
//     y1: PropTypes.number.isRequired
// };

export default VendorTreeMap;