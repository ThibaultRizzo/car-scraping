import React from 'react';
import { Layout, Menu, Icon, Button, Row, Col } from 'antd';
import { Link, withRouter } from 'react-router-dom'
import { connect } from 'react-redux';
import * as actions from '../store/actions/auth';

const { Header, Content, Sider, Footer } = Layout;
const SubMenu = Menu.SubMenu;

class CustomLayout extends React.Component {
    state = {
        collapsed: true,
    };

    onCollapse = (collapsed) => {
        this.setState({ collapsed });
    }

    render() {
        return (
            <Layout style={{ minHeight: '100vh' }}>
                <Header className="header">
                    <div className="logo" />
                    <Row type="flex" justify="end" align="middle" gutter={16}>
                        <Col><Button disabled type="primary" shape="circle" icon="user" size='large' /></Col>
                        <Col><Button disabled type="primary" shape="circle" icon="ellipsis" size='large' /></Col>
                    </Row>
                    {/* <Menu
                        theme="dark"
                        mode="horizontal"
                        defaultSelectedKeys={['2']}
                        style={{ lineHeight: '64px' }}
                        type="flex"
                        justify="end"
                    >
                        <Menu.Item key="1">nav 1</Menu.Item>
                        <Menu.Item key="2">nav 2</Menu.Item>
                        <Menu.Item key="3">nav 3</Menu.Item>
                    </Menu> */}
                </Header>
                <Layout>
                    <Sider
                        collapsible
                        collapsed={this.state.collapsed}
                        onCollapse={this.onCollapse}
                    >
                        <div className="logo" />
                        <Menu theme="dark" defaultSelectedKeys={['2']} mode="inline">
                            <Menu.Item key="1">
                                <Icon type="home" />
                                <span><Link style={{ color: 'white' }} to={"/"}>Home</Link></span>
                            </Menu.Item>
                            <SubMenu
                                key="sub1"
                                title={<span><Icon type="car" /><span>Cars</span></span>}
                            >
                                <Menu.Item key="2">
                                    <Icon type="pie-chart" />
                                    <span><Link style={{ color: 'white' }} to={"/cars/"}>Chart</Link></span>
                                </Menu.Item>
                            </SubMenu>
                            <SubMenu
                                key="sub2"
                                title={<span><Icon type="team" /><span>Other Random Category</span></span>}
                            >
                            </SubMenu>
                        </Menu>
                    </Sider>
                    <Content style={{ margin: '0 16px' }}>
                        {this.props.children}
                    </Content>
                </Layout>
                <Footer>Footer</Footer>
            </Layout>
        );
    }
}

const mapDispatchToProps = dispatch => {
    return {
        logout: () => dispatch(actions.logout())
    }
}

export default withRouter(connect(null, mapDispatchToProps)(CustomLayout));