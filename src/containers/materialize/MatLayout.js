import React from 'react';
import { Link, withRouter } from 'react-router-dom'

import { ReactComponent as Logo } from '../../img/logo-Pack-blanc.svg';
import './MatLayout.scss';

import { Navbar, NavItem, Icon, Collection, CollectionItem } from 'react-materialize'



const MatNavbar = (props) => {
    return (
        <Navbar className="blue-grey darken-3" brand={<Logo className="col" style={{ height: "50%" }} />} right>
            <NavItem href='get-started.html'><Icon color="white">account_circle</Icon></NavItem>
            <NavItem href='get-started.html'><Icon color="white">more_vert</Icon></NavItem>
        </Navbar>
    );
}

const MatCollection = (props) => {
    return (
        <Collection className="sidenav-col col m2">
            {/* <CollectionItem className="row blue-grey-text text-darken-3">
                <Icon className="col">home</Icon>
                <span><Link style={{ color: 'white' }} to={"/"}>Home</Link></span>
            </CollectionItem> */}
            <MatLink
                className="row blue-grey-text text-darken-3"
                icon="home"
                color="white"
                path="/"
                name="Home"
            />
            <MatLink
                className="item-active row blue-grey-text text-darken-3"
                icon="airport_shuttle"
                color="white"
                path="/carspreview/"
                name="Cars"
            />
            <MatLink
                className="item-active row blue-grey-text text-darken-3"
                icon="bar_chart"
                color="white"
                path="/chart/"
                name="Charts"
            />
            <MatLink
                className="item-active row blue-grey-text text-darken-3"
                icon="table_chart"
                color="white"
                path="/table/"
                name="Tables"
            />
            <MatLink
                className="item-active row blue-grey-text text-darken-3"
                icon="email"
                color="white"
                path="/report/"
                name="Report"
                disabled
            />
            <MatLink
                className="item-active row blue-grey-text text-darken-3"
                icon="how_to_vote"
                color="white"
                path="/scrap/"
                name="Scrap"
            />
            <MatLink
                className="item-active row blue-grey-text text-darken-3"
                icon="settings"
                color="white"
                path="/settings/"
                name="Settings"
            />
        </Collection>
    );
}

const MatLink = ({ icon, color, path, name, active = false, ...props }) => {
    const styles = {
        linkStyle: {
            color: color,
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            marginBottom: '0px',
            textDecoration: 'none'
        },
        itemStyle: {
            listStyle: 'none',
            borderBottom: 'none',
            transition: 0.25
        }
    }
    return (
        <CollectionItem style={styles.itemStyle} className="link-item">
            <Link style={styles.linkStyle} to={path} {...props}>
                <Icon className="col">{icon}</Icon>
                <span>
                    {name}
                </span>
            </Link>
        </CollectionItem >
    );
}


class MatLayout extends React.Component {
    state = {

    }

    render() {
        return (
            <div>
                <MatNavbar />
                <div className="row">
                    <MatCollection />
                    <div className="col m10">
                        {this.props.children}
                    </div>
                </div>
            </div>
        );
    }
}

export default withRouter(MatLayout);