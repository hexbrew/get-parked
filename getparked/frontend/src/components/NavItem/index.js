import React from "react";
import "./NavItem.scss"

export class NavItem extends React.Component {
    render() {
        return <a className="nav-item" href="http://www.google.com" target="_blank">{this.props.name}</a>
    }
}