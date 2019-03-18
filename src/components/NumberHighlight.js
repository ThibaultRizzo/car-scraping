import React from 'react';
import { Card, Icon } from 'react-materialize';
import { CarStatisticTitle } from '../enums';

import './NumberHighlight.scss'

const NumberHighlight = ({ data, layoutClass, color, ...props }) => {
    const { title, number, unit, trend } = data;
    const getTrendIcon = (trend) => {
        switch (trend) {
            // TODO: Add enums
            case "ASC": return <span style={{ color: "#31e831" }}><Icon>trending_up</Icon></span>
            case "DESC": return <span style={{ color: "red" }}><Icon>trending_down</Icon></span>
            case "FLAT": return <span style={{ color: "white" }}><Icon >trending_flat</Icon></span >
            default:
        }
    }
    return (
        <div className={layoutClass}>
            <Card
                className='blue-grey darken-1'
                textClassName='white-text'
                title={<strong className="white-text">{`${Math.floor(number)} ${unit}`}</strong>}
                // actions={[<span key={"actions" + number}> {Trend[trend]}</span>]}
                actions={[<span style={{ fontSize: '20px' }} className="center-align" key={"actions" + number}> {getTrendIcon(trend)}</span>]}
                {...props}
                style={{ background: color }}
            >
                {CarStatisticTitle[title]}
            </Card>
        </div >
    );
}

export default NumberHighlight;