import React from 'react';
import './header.css';
import { useNavigate } from 'react-router-dom';

function Header() {
    const navigate = useNavigate();

    const handleProfileClick = (event) => {
        event.preventDefault();
        navigate('/Profile');
    };

    return (
        <header className="header">
            <div className="logo-container">
                <img src='../../imgs/Namix.png' alt='Логотип'/>
            </div>
            <div className="content-wrapper">
                <h1>Title</h1>
                <p className="subtitle">Сабтайтл</p>
            </div>
            <div className="profile-container">
                <span className="profile"><a href="#" onClick={handleProfileClick}>Profile</a></span>
            </div>
        </header>
    );
}

export default Header;