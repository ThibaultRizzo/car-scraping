import React from 'react';
import { Card } from 'react-materialize';

const NumberHighlight = ({ data, layoutClass }) => {
    const { title, number, content } = data;
    return (
        <div className={layoutClass}>
            <Card
                className='blue-grey darken-1'
                textClassName='white-text'
                title={title}
                actions={[<span>{number}</span>]}>
                {content}
            </Card>
        </div>
    );
}

export default NumberHighlight;