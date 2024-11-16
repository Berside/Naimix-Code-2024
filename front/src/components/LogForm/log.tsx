import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Home from '../Home/Home';
import './log.css';
import { login } from '../../utils/login';
import endpoints from '../../utils/endpoints';

const LoginForm = () => {
  const navigate = useNavigate();
  
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await login(email, password);
      console.log(response)
      if (response && response.token) {
        localStorage.setItem('token', response.token);
      } else {
        throw new Error('No token found in the response');
      }
      navigate('/Home');
    } catch (error) {
      console.error('Error:', error);
      alert('Произошла ошибка при входе в систему. Пожалуйста, попробуйте снова.');
    }
  };
  return (
    <form className="form-log" onSubmit={handleSubmit}>
      <h2>Вход в систему</h2>
      <div>
        <label htmlFor="email">Email:</label>
        <input type="email" id="email" value={email} onChange={(e) => setEmail(e.target.value)} required/>
      </div>

      <div>
        <label htmlFor="password">Пароль:</label>
        <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} required/>
      </div>

      <button type="submit">Войти</button>
      <a onClick={() => navigate('/Reg')}>Нет аккаунта, зарегистрируйся!</a>
    </form>
  );
};

export default LoginForm;
