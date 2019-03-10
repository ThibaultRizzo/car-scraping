import React from 'react';
import axios from 'axios';
import * as constants from '../../constants';

import { ReactComponent as Logo } from '../../img/logo-Pack-blanc.svg';
import './MatContainer.scss';


import { Navbar, NavItem, Icon, Collection, CollectionItem } from 'react-materialize'
import NumberHighlight from '../../components/NumberHighlight';
import TreeMap from '../../components/data-visualisation/TreeMap';
import BoxPlot from '../../components/data-visualisation/BoxPlot';

const MatNavbar = (props) => {
    return (
        <Navbar className="blue-grey darken-3" brand={<Logo className="col" style={{ height: "50%" }} />} right>
            <NavItem href='get-started.html'><Icon color="white">account_circle</Icon></NavItem>
            <NavItem href='get-started.html'><Icon color="white">more_vert</Icon></NavItem>
        </Navbar>
    );
}

const MatContent = (props) => {
    return (
        <div className="row">
            <MatCollapsible />
            <MatContainer />
        </div>
    );
}

const MatCollapsible = (props) => {
    return (
        <Collection className="sidenav-col col m2">
            <CollectionItem className="row blue-grey-text text-darken-3" href='#'><Icon className="col">home</Icon><span className="col">Home</span></CollectionItem>
            <CollectionItem className="item-active row blue-grey-text text-darken-3" href='#' active><Icon className="col">airport_shuttle</Icon><span className="col">Cars</span></CollectionItem>
        </Collection>
    );
}

class MatContainer extends React.Component {
    state = {
        numbers: [],
        treemaps: [],
        boxplot: []
    }

    componentWillMount() {
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
            <div className="col m10">
                <MatNumberHighlightListView data={numbers} className="row m3" />
                <MatTreemapListView data={treemaps} className="row m4" />
                <MatBoxPlotListView data={boxplot} className="row m3" />
                <div className="container"></div>
            </div>
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

const MatTreemapListView = ({ data, ...props }) => {
    const treemapData = [{}];
    return (
        <div {...props}>
            {treemapData.map((data, id) => <TreeMap treeData={data} key={"tr-" + id} />)}
        </div>
    );
}

const MatBoxPlotListView = ({ data, ...props }) => {
    const boxPlotData = [{}];
    return (
        <div {...props}>
            <BoxPlot data={boxPlotData} />
        </div>
    );
}

export { MatNavbar, MatContent };