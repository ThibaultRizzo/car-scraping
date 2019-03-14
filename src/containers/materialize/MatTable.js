import React from 'react';
import axios from 'axios';
import * as constants from '../../constants';
import { Table, Pagination } from 'react-materialize'

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

    render() {
        const keysList = this.state.data.length > 0 ? Object.getOwnPropertyNames(this.state.data[0]) : [];
        return (
            <>
                <h2 className="center-align row">Tables</h2>
                <Pagination className="right-align row" items={10} activePage={this.state.page} maxButtons={8} onSelect={num => this.loadData(num)} />
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