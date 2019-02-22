import React from 'react';
import axios from 'axios';
import { connect } from 'react-redux';
import { Card, Button } from 'antd';
import CustomForm from '../components/Form';

class ArticleDetail extends React.Component {
    state = {
        article: {}
    }

    componentWillReceiveProps(newProps) {
        if (newProps.token) {
            axios.defaults.headers = {
                'Content-Type': 'application/json',
                Authorization: newProps.token
            }
            const articleID = this.props.match.params.articleID;
            axios.get(`http://127.0.0.1:8000/api/${articleID}/`)
                .then(res => {
                    this.setState({ article: res.data });
                }
                )
        }
    }

    handleDeletion = (event) => {
        event.preventDefault();
        if (this.props.token !== null) {
            const articleID = this.props.match.params.articleID;
            axios.defaults.headers = {
                'Content-Type': 'application/json',
                Authorization: `Token ${this.props.token}`
            }
            axios.delete(`http://127.0.0.1:8000/api/${articleID}/`);
            this.props.history.push('/');
            this.forceUpdate();
        } else {

        }
    }

    render() {
        const articleID = this.props.match.params.articleID;
        return (
            <>
                <Card title={this.state.article.title}>
                    <p>{this.state.article.content}</p>
                </Card>
                <CustomForm requestType="put" articleID={articleID} btnText="Update" />
                <form onSubmit={this.handleDeletion}>
                    <Button type="danger" htmlType="submit">Delete</Button>
                </form>
            </>
        );
    }
}


const mapStateToProps = state => {
    return {
        token: state.token
    }
}

export default connect(mapStateToProps)(ArticleDetail)

