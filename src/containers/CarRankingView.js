import React from 'react';
import axios from 'axios';
import TableView from './TableView';
import ChartView from './ChartView';

class CarRankingView extends React.Component {
    state = {
        cars: []
    }

    componentDidMount() {
        // Get the car data from server
        axios.get(`http://127.0.0.1:8000/car-api/`)
            .then(res => {
                this.setState({ cars: res.data });
                console.dir(res);
            })
    }

    render() {
        return (
            <div style={layoutStyleSheet}>
                <ChartView />
                <TableView data={this.state.cars} />
            </div>
        );
    }
}


const layoutStyleSheet = {
    display: 'flex',
    flexFlow: 'column nowrap',
    justifyContent: 'flex-start'
};

export default CarRankingView;