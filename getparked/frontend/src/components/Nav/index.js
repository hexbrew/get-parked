import React from "react";
import "./Nav.scss";
import { NavItem } from "../NavItem"

export class Nav extends React.Component {
    render() {
        return <nav id="main-nav">
            <ul>
                <li><NavItem name="Home" /></li>
                <li><NavItem name="Car Parks" /></li>
                <li><NavItem name="About" /></li>
                <li><NavItem name="News" /></li>
                <li><NavItem name="Contact" /></li>
            </ul>
        </nav>;
    }
}