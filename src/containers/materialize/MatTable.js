import React from 'react';
import axios from 'axios';
import * as constants from '../../constants';
import { Row, Button, Table, Pagination } from 'react-materialize'

export default class MatTable extends React.Component {
    state = {
        data: [],
        pageNb: 1,
        maxPageNb: 10
    }

    componentDidMount() {
        this.loadData(this.state.pageNb);
    }

    loadData = (pageNb) => {
        this.setState({ pageNb: pageNb })
        axios.get(constants.PAGINATED_CARS_URL + pageNb)
            .then(res => {
                this.setState({
                    data: res.data.results,
                    maxPageNb: Math.floor(res.data.count / res.data.limit)
                });
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
        const url = window.URL.createObjectURL(new Blob([this.state.csv]));
        const link = document.createElement('a');
        link.href = url;
        const today = new Date();
        link.setAttribute('download', `car_list_${today.getFullYear()}_${today.getMonth()}_${today.getDate()}.csv`);
        document.body.appendChild(link);
        link.click();
    }

    render() {
        const keysList = this.state.data.length > 0 ? Object.getOwnPropertyNames(this.state.data[0]) : [];
        return (
            <>
                <h2 className="center-align row">Tables</h2>
                <Row>
                    <Pagination className="right-align offset-s1" items={this.state.maxPageNb} activePage={this.state.page} maxButtons={10} onSelect={num => this.loadData(num)} />
                </Row>
                <Table>
                    <thead>
                        <tr>
                            {keysList.map((key, i) => <th data-field={key} key={"header" + i}>{constants.CAR_LABEL_DICT[key]}</th>)}
                        </tr>
                    </thead>

                    <tbody>
                        {this.state.data.map((el, i) => <CarRow key={"row" + i} data={el} />)}
                    </tbody>
                </Table>
                <Button floating fab='vertical' onClick={this.loadCsv} icon='file_download' waves='red' className='text-white blue-grey darken-3' large style={{bottom: '45px', right: '24px'}}/>
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