import React from 'react';
import './header.css';


const Header = ({ title, subtitle, logoImage, profileText }) => {
  return (
    <header className="header">
      <div className="logo-container">
        <img src='../../imgs/Namix.png' alt='Логотип'/>
      </div>
      <div className="content-wrapper">
        <h1>{title}</h1>
        {subtitle && <p className="subtitle">{subtitle}</p>}
      </div>
      <div className="profile-container">
        <span className="profile">Profile</span>
      </div>
    </header>
  );
};

export default Header;
