import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Home from '../Home/Home';


const LoginForm = ({ onLogin }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async(e) => {
    e.preventDefault();
    try{
        if (onLogin) {
        onLogin({ email, password });
        navigate('/Home');
        }
        navigate('/home')
            const LoginData = {
                email,
                password
            };
            navigate('/Home', { state: { from: '/Login' } });
    } catch (error) {
      console.error('Ошибка при регистрации:', error);
      alert('Произошла ошибка при регистрации. Пожалуйста, попробуйте снова.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
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
    </form>
  );
};
export default LoginForm;
