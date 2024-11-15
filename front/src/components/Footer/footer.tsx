import React from 'react';
import { Link } from 'react-router-dom';
import './footer.css';
const Footer = () => {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer__top">
          <ul className="social-links">
            <li><a href="https://www.facebook.com" target="_blank" rel="noopener noreferrer">Facebook</a></li>
            <li><a href="https://twitter.com" target="_blank" rel="noopener noreferrer">Twitter</a></li>
            <li><a href="https://instagram.com" target="_blank" rel="noopener noreferrer">Instagram</a></li>
          </ul>
        </div>

        <div className="footer__bottom">
          <div className="footer__column footer__column_left">
            <h3>О нас</h3>
            <p>Мы - компания, специализирующаяся на разработке веб-приложений.</p>
          </div>

          <div className="footer__column footer__column_center">
            <h3>Информация</h3>
            <ul>
              <li><Link to="/returns-policy">Политика возврата</Link></li>
              <li><Link to="/terms-and-conditions">Условия использования</Link></li>
              <li><Link to="/contact">Контакты</Link></li>
            </ul>
          </div>
          <div className="footer__column footer__column_right">
            <h3>Свяжитесь с нами</h3>
            <p>Телефон: +7 701 732 01 10</p>
            <p>Email: info@ourcompany.com</p>
          </div>
        </div>
      </div>
      <div className="footer-separator"></div>
    </footer>
  );
};

export default Footer;
