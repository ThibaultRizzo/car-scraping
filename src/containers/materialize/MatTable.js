import React from 'react';
import axios from 'axios';
import * as constants from '../../constants';
import { Icon, Row, Button, Table, Pagination } from 'react-materialize'

export default class MatTable extends React.Component {
    state = {
        data: [],
        pageNb: 1,
        maxPageNb: 10,
        isDiscovered: true
    }

    componentDidMount() {
        this.loadData(this.state.pageNb);
    }

    discover = () => {
        this.setState({ isDiscovered: false });
    }

    undiscover = () => {
        this.setState({ isDiscovered: true });
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
        // Removing columns not wanted
        const UNWANTED_FIELDS = ['owner_number', 'reg_number', 'reg_date'];
        return (
            <div onClick={this.discover}>
                <h2 className="center-align row">Tables</h2>
                <Row>
                    <Pagination className="center-align right-align offset-s1" items={this.state.maxPageNb} activePage={this.state.page} maxButtons={10} onSelect={num => this.loadData(num)} />
                </Row>
                {
                    this.state.isDiscovered
                        ? (
                            <Button floating onClick={this.loadCsv} icon='file_download' waves='red' className='text-white blue-grey darken-3 btn-floating pulse' large style={{ position: 'fixed', bottom: '2%', right: '2%' }} />
                        )
                        : (
                            <Button floating onClick={this.loadCsv} icon='file_download' waves='red' className='text-white blue-grey darken-3' large style={{ position: 'fixed', bottom: '2%', right: '2%' }} />
                        )
                }
                {/* <MatUpload isDiscovered={this.state.isDiscovered} /> */}
                <Table style={{ fontSize: '0.8em' }}>
                    <thead>
                        <tr>
                            {keysList.filter(el => !UNWANTED_FIELDS.includes(el)).map((key, i) => <th data-field={key} key={"header" + i}>{constants.CAR_LABEL_DICT[key]}</th>)}
                        </tr>
                    </thead>

                    <tbody>
                        {this.state.data.map((el, i) => <CarRow key={"row" + i} data={el} />)}
                    </tbody>
                </Table>
                {/* */}
            </div>
        );
    }
}

const CarRow = ({ data = {} }, key) => {
    return (
        <tr key={key}>
            {Object.entries(data).map((arr, i) => {
                switch (arr[0]) {
                    case 'vendor_link': return <td key={key + "-data" + i}><a href={arr[1]} target="_blank" rel="noopener noreferrer"><Icon color="white">link</Icon></a></td>;
                    case 'owner_number': case 'reg_number': case 'reg_date': return false;
                    default: return <td key={key + "-data" + i}>{arr[1]}</td>;
                }
            })
            }
        </tr>);
}