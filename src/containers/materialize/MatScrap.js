import React from 'react';
import axios from 'axios';
import * as constants from '../../constants';

import { Row, Col, ProgressBar } from 'react-materialize'

export default class MatScrap extends React.Component {
    state = {
        isLoading: false
    }
    componentDidMount() {
        window.confirm("Do you really want to launch a scraping process? This will erase the current data in Car table...")
            && this.scrapCarData();
    }

    scrapCarData = () => {
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