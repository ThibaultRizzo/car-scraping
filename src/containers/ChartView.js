import React from 'react';
import TreeMap from '../components/data-visualisation/TreeMap';

class ChartView extends React.Component {
    state = {
        data: [
            { id: '5fbmzmtc', x: 7, y: 41, z: 6 },
            { id: 's4f8phwm', x: 11, y: 45, z: 9 },
            // ...
        ],
        domain: { x: [0, 30], y: [0, 100] }
    };

    // data = {
    //     labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    //     datasets: [{
    //         label: '# of Votes',
    //         data: [12, 19, 3, 5, 2, 3],
    //         backgroundColor: [
    //             'rgba(255, 99, 132, 0.2)',
    //             'rgba(54, 162, 235, 0.2)',
    //             'rgba(255, 206, 86, 0.2)',
    //             'rgba(75, 192, 192, 0.2)',
    //             'rgba(153, 102, 255, 0.2)',
    //             'rgba(255, 159, 64, 0.2)'
    //         ],
    //         borderColor: [
    //             'rgba(255,99,132,1)',
    //             'rgba(54, 162, 235, 1)',
    //             'rgba(255, 206, 86, 1)',
    //             'rgba(75, 192, 192, 1)',
    //             'rgba(153, 102, 255, 1)',
    //             'rgba(255, 159, 64, 1)'
    //         ],
    //         borderWidth: 1
    //     }]
    // };

    render() {
        return (
            // <Chart data={data}/>
            <TreeMap
                width="1000"
                height="500"
                data={this.state.data}
                domain={this.state.domain} />
        );
    }
}

export default ChartView;