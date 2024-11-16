import React from 'react';
import { Link } from 'react-router-dom';
import './footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-links">
        <ul>
          <li>Разделы</li>
          <li><Link to='/'> О нас </Link></li>
          <li><Link to='/'> Каталог </Link></li>
          <li><Link to='/'> Файлы </Link></li>
          <li><Link to='/'> Услуги </Link></li>
        </ul>
        <ul>
          <li>О предприятии</li>
          <li><Link to='/'> Продукция </Link></li>
          <li><Link to='/'> Новости </Link></li>
          <li><Link to='/'> Поддержка </Link></li>
        </ul>
        <ul>
        <li>Контакты</li>
        <li>+7 495 425-24-21<br />Телефон по Свердловска</li>
        <li>+7 800 120-32-59<br />Бесплатный телефон по России</li>
      </ul>
       <ul>
        <li>E-mail</li>
        <li>pionerrro@sila.ru</li>
      </ul>
      </div>
    </footer>
  );
};

export default Footer;
