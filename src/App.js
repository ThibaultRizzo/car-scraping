import React, { Component } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import { connect } from 'react-redux';
// import CustomLayout from './containers/Layout';
import BaseRouter from './routes';
import 'antd/dist/antd.css';
import * as actions from './store/actions/auth';

import MatLayout from './containers/materialize/MatLayout';
import './App.scss';

class App extends Component {

  componentDidMount() {
    this.props.onTryAutoSignup();
  }

  render() {
    return (
      <div className="App" style={{ height: "100%" }}>
        {/* <Router>
          <CustomLayout {...this.props}>
            <BaseRouter />
          </CustomLayout>
        </Router> */}
        {/* <MatNavbar /> */}
        <Router>
          <MatLayout>
            <BaseRouter />
          </MatLayout>
        </Router>

      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    isAuthenticated: state.token !== null
  }
}

const mapDispatchToProps = dispatch => {
  return {
    onTryAutoSignup: () => dispatch(actions.authCheckState())
  };
}


export default connect(mapStateToProps, mapDispatchToProps)(App);
