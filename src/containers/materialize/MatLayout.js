import React from 'react';
import { Link, withRouter } from 'react-router-dom'

import { ReactComponent as Logo } from '../../img/logo-Pack-blanc.svg';
import './MatLayout.scss';

import { Navbar, NavItem, Icon, Collection, CollectionItem, Footer } from 'react-materialize'


// Add theme to context
const MatNavbar = ({ theme }) => {
    return (
        <Navbar className={theme} brand={<Logo className="col" style={{ height: "50%" }} />} right>
            <NavItem className="disabled"><Icon color="white">account_circle</Icon></NavItem>
            <NavItem><Icon color="white">more_vert</Icon></NavItem>
            <NavItem className="hide-on-large-only" href="/"><Icon color="white">home</Icon>Home</NavItem>
            <NavItem className="hide-on-large-only" href="/chart/"><Icon color="white">bar_chart</Icon>Charts</NavItem>
            <NavItem className="hide-on-large-only" href="/table/"><Icon color="white">table_chart</Icon>Tables</NavItem>
        </Navbar>
    );
}

const MatCollection = (props) => {
    return (
        <Collection className="sidenav-col col m2 hide-on-med-and-down">
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
            {/* <MatLink
                className="item-active row blue-grey-text text-darken-3"
                icon="airport_shuttle"
                color="white"
                path="/carspreview/"
                name="Cars"
            /> */}
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
            {/* <MatLink
                className="item-active row blue-grey-text text-darken-3"
                icon="email"
                color="white"
                path="/report/"
                name="Report"
                disabled
            /> */}
            <MatLink
                className="item-disabled row blue-grey-text text-darken-3"
                icon="how_to_vote"
                color="white"
                path="/scrap/"
                name="Scrap"
                disabled
            />
            <MatLink
                className="item-active row blue-grey-text text-darken-3"
                icon="settings"
                color="white"
                path="/settings/"
                name="Settings"
                disabled
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

const MatFooter = ({ theme }) => {
    return (
        <Footer
            className={theme}
            copyrights="Copyright Pack. &copy; 2019"
        >
            <a href="http://team-pack.fr" target="_blank" rel="noopener noreferrer"><h5 className="white-text">Pack.</h5></a>
        </Footer>
    );
}


class MatLayout extends React.Component {
    state = {
        theme: "blue-grey darken-3"
    }

    render() {
        return (
            <div>
                <MatNavbar theme={this.state.theme} />
                <div className="row">
                    <MatCollection />
                    <div className="col l10 m12">
                        {this.props.children}
                    </div>
                </div>
                <MatFooter theme={this.state.theme} />
            </div>
        );
    }
}

export default withRouter(MatLayout);