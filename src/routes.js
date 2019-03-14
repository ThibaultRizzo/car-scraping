import React from 'react';
import { Route } from 'react-router-dom';
import HomePage from './containers/HomePage';
// import Login from './containers/Login';
// import Signup from './containers/Signup';
// import CarRankingView from './containers/CarRankingView';
import { MatChart } from './containers/materialize/MatChart';
import MatTable from './containers/materialize/MatTable';
import MatScrap from './containers/materialize/MatScrap';

const BaseRouter = () => (
    <div>
        <Route exact path='/' component={HomePage} />
        {/* <Route exact path='/login/' component={Login} />
        <Route exact path='/signup/' component={Signup} /> */}

        <Route exact path='/chart/' component={MatChart} />
        <Route exact path='/table/' component={MatTable} />
        <Route exact path='/scrap/' component={MatScrap} />
    </div>
);

export default BaseRouter;