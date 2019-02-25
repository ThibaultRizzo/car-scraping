import React from 'react';
import { Layout, Menu, Breadcrumb, Icon } from 'antd';
import { Link, withRouter } from 'react-router-dom'
import { connect } from 'react-redux';
import * as actions from '../store/actions/auth';

const { Header, Content, Sider } = Layout;
const SubMenu = Menu.SubMenu;

class CustomLayout extends React.Component {
    state = {
        collapsed: false,
    };

    onCollapse = (collapsed) => {
        console.log(collapsed);
        this.setState({ collapsed });
    }

    render() {
        return (
            <Layout style={{ minHeight: '100vh' }}>
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
                <Layout>
                    <Header style={{ background: '#fff', padding: 0 }} />
                    <Content style={{ margin: '0 16px' }}>
                        <Breadcrumb style={{ margin: '16px 0' }}>
                            <Breadcrumb.Item><Link to={"/"}>Home</Link></Breadcrumb.Item>
                            <Breadcrumb.Item><Link to={"/cars/"}>Cars</Link></Breadcrumb.Item>
                        </Breadcrumb>
                        <div style={{ background: '#fff', padding: 24, minHeight: 280 }}>
                            {this.props.children}
                        </div>
                    </Content>
                </Layout>
            </Layout >
        );
    }
}

const mapDispatchToProps = dispatch => {
    return {
        logout: () => dispatch(actions.logout())
    }
}

export default withRouter(connect(null, mapDispatchToProps)(CustomLayout));