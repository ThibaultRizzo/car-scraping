import React from 'react';
import axios from 'axios';
import * as constants from '../../constants';

import { Row, Col, ProgressBar } from 'react-materialize'

export default class MatScrap extends React.Component {
    state = {
        isLoading: false
    }
    componentDidMount() {
        this.setState({ isLoading: true });
        axios.get(constants.SCRAPING_URL)
            .then(res => {
                this.setState({ isLoading: false });
            });

    }

    render() {
        return (
            <Row>
                <Col s={12}>
                    {this.state.isLoading
                        ? <ProgressBar />
                        : <div> Scraped !</div>
                    }
                </Col>
            </Row>
        );
    }
}