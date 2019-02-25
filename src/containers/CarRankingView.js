import React from 'react';
import TableView from './TableView';
import ChartView from './ChartView';

class CarRankingView extends React.Component {
    state = {
        cars: []
    }

    componentDidMount() {
        // Get the car data from server
    }

    render() {
        return (
            <div style={layoutStyleSheet}>
                <ChartView />
                <TableView />
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