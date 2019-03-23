import React from "react";
import { Nav } from "../Nav"
import './Header.scss'

export class Header extends React.Component {
    state = {};

    render() {
        return <header id="page-header" >
            <h1>Get Parked</h1>
            <Nav />
        </header>;
    }
}