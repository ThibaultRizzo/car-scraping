import React from 'react';
import MaterialIcon, { colorPalette } from 'material-icons-react';
import { ReactComponent as Logo } from '../../img/logo-Pack-blanc.svg';
import './MatContainer.css';

const MatNavbar = (props) => {
    return (
        <nav class="indigo lighten-2">
            <div class="nav-wrapper">
                <a href="#!" class="brand-logo">
                    <Logo style={{ height: '80%' }} />
                </a>
                <ul class="right hide-on-med-and-down">
                    <li><a href="sass.html">
                        <MaterialIcon icon="search" />
                    </a></li>
                    <li><a href="badges.html">
                        <MaterialIcon icon="view_module" />
                    </a></li>
                    <li><a href="collapsible.html">
                        <MaterialIcon icon="refresh" />
                    </a></li>
                    <li><a href="mobile.html">
                        <MaterialIcon icon="more_vert" />
                    </a></li>
                </ul>
            </div>
        </nav>
    );
}

export { MatNavbar };