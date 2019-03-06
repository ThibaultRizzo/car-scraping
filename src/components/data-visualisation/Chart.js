import React from 'react';
// import { Bar } from 'react-chartjs-2';

const Chart = ({ data }) => {
    return (
        <div
            data={data}
            width={100}
            height={50}
            options={{
                maintainAspectRatio: false
            }}
        />
    );
};

export default Chart;