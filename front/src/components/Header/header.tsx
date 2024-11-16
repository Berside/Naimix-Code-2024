import React from 'react';
import './header.css';
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import logo from '../../imgs/Namix.png'
function Header() {
    const navigate = useNavigate();

    const handleProfileClick = (event) => {
        event.preventDefault();
        navigate('/Profile');
    };
    return (
        <header className="header">
            <div className="logo-container">
                <img src={logo} alt='Логотип' className="logo-image"/>
            </div>
        <nav className="navbar">
            {/* <a><Link to='/'> Услуги </Link></a>
            <a><Link to='/'> Продукция </Link></a>
            <a><Link to='/'> О предприятии </Link></a>
            <a><Link to='/'> Помощь </Link></a> */}
        </nav>
            <div className="icons">
                <span className="icon icon-home"><a href="#" onClick={handleProfileClick}>🏠</a></span>
            </div>
        </header>
    );
}
export default Header;