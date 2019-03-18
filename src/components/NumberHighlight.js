import React from 'react';
import { Card, Icon } from 'react-materialize';
import { CarStatisticTitle } from '../enums';

const NumberHighlight = ({ data, layoutClass, color, ...props }) => {
    const { title, number, unit, trend } = data;
    const getTrendIcon = (trend) => {
        switch (trend) {
            // TODO: Add enums
            case "ASC": return <span style={{ color: "#31e831" }}><Icon>trending_up</Icon></span>
            case "DESC": return <span style={{ color: "red" }}><Icon>trending_down</Icon></span>
            case "FLAT": return <span style={{ color: "black" }}><Icon >trending_flat</Icon></span >
            default:
        }
    }
    return (
        <div className={layoutClass}>
            <Card
                className='blue-grey darken-1'
                textClassName='white-text'
                title={`${Math.floor(number)} ${unit}`}
                // actions={[<span key={"actions" + number}> {Trend[trend]}</span>]}
                actions={[<span className="center-align" key={"actions" + number}> {getTrendIcon(trend)}</span>]}
                {...props}
                style={{ background: color }}
            >
                {CarStatisticTitle[title]}
            </Card>
        </div >
    );
}

export default NumberHighlight;