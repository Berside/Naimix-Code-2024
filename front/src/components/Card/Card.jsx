import React from 'react';
import './Card.css';
import { useNavigate } from 'react-router-dom';
const Card = ({ name, zodiacSign, age }) => {
    const navigate = useNavigate();
    const handleRaz = (event) => {
        event.preventDefault();
        navigate('/Main');
    };

  return (
    <div className="employee-card">
      <h3>Информация о сотруднике</h3>
      <p><strong>Имя:</strong> {name}</p>
      <p><strong>Знак зодиака:</strong> {zodiacSign}</p>
      <p><strong>Возраст:</strong> {age} лет</p>
      <a onClick={handleRaz}>&gt;</a> 
    </div>
  );
};
export default Card;
