import React from 'react';
import './header.css';
import { Link } from 'react-router-dom';

const Header = ({ title, subtitle, logoImage, profileText }) => {
  return (
    <header className="header">
      <div className="logo-container">
        <img src='../../imgs/Namix.png' alt='Логотип' className="logo-image"/>
      </div>
      <nav className="navbar">
        <a><Link to='/'> Услуги </Link></a>
        <a><Link to='/'> Продукция </Link></a>
        <a><Link to='/'> О предприятии </Link></a>
        <a><Link to='/'> Помощь </Link></a>
      </nav>
      <div className="icons">
        <span className="icon icon-home">🏠</span>
      </div>
    </header>
  );
};


export default Header;