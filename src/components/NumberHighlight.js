import React from 'react';
import { Card } from 'react-materialize';
import { CarStatisticTitle, Trend } from '../enums';

const NumberHighlight = ({ data, layoutClass, color, ...props }) => {
    const { title, number, unit, trend } = data;
    return (
        <div className={layoutClass}>
            <Card
                className='blue-grey darken-1'
                textClassName='white-text'
                title={`${Math.floor(number)} ${unit}`}
                actions={[<span key={"actions" + number}> {Trend[trend]}</span>]}
                {...props}
                style={{ background: color }}
            >
                {CarStatisticTitle[title]}
            </Card>
        </div >
    );
}

export default NumberHighlight;