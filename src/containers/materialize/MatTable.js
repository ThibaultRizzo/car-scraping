import React from 'react';
import axios from 'axios';
import * as constants from '../../constants';
import { Row, Button, Table, Pagination } from 'react-materialize'

export default class MatTable extends React.Component {
    state = {
        data: [],
        pageNb: 1
    }

    componentDidMount() {
        this.loadData(this.state.pageNb);
    }

    loadData = (pageNb) => {
        this.setState({ pageNb: pageNb })
        axios.get(constants.PAGINATED_CARS_URL + pageNb)
            .then(res => {
                this.setState({ data: res.data.results });
            });
    }

    /**
     * Load the csv in state, else download csv file of all cars in DB
     */
    loadCsv = () => {
        if (this.state.csv) {
            this.downloadCsv()
        } else {
            axios.get(constants.CAR_CSV_URL)
                .then(res => {
                    this.setState({ csv: res.data });
                    this.downloadCsv();
                });
        }
    }

    /***
     * Triggers a download form the browser by adding a link and clicking on it
     */
    downloadCsv = () => {
        const url = window.URL.createObjectURL(new Blob([this.state.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', `car_list_${new Date()}.csv`);
        document.body.appendChild(link);
        link.click();
    }

    render() {
        const keysList = this.state.data.length > 0 ? Object.getOwnPropertyNames(this.state.data[0]) : [];
        return (
            <>
                <h2 className="center-align row">Tables</h2>
                <Row>
                    <Button className="left-align col m1" type="primary" onClick={this.loadCsv}>Export as CSV</Button>
                    <Pagination className="right-align offset-s1" items={10} activePage={this.state.page} maxButtons={8} onSelect={num => this.loadData(num)} />
                </Row>
                <Table>
                    <thead>
                        <tr>
                            {keysList.map((key, i) => <th data-field={key} key={"header" + i}>{key}</th>)}
                        </tr>
                    </thead>

                    <tbody>
                        {this.state.data.map((el, i) => <CarRow key={"row" + i} data={el} />)}
                    </tbody>
                </Table>
            </>
        );
    }
}

const CarRow = ({ data = {} }, key) => {
    return (
        <tr key={key}>
            {Object.values(data).map((val, i) => <td key={key + "-data" + i}>{val}</td>)}
        </tr>);
}