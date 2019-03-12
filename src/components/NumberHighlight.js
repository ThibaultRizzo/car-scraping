import React from 'react';
import { Card } from 'react-materialize';

const NumberHighlight = ({ data, layoutClass, ...props }) => {
    const { title, number, content } = data;
    return (
        <div className={layoutClass}>
            <Card
                className='blue-grey darken-1'
                textClassName='white-text'
                title={title}
                actions={[<span key={"actions" + number}> {number}</span>]}
                {...props}
            >
                {content}
            </Card>
        </div >
    );
}

export default NumberHighlight;