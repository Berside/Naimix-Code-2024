import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './reg.css'
import { post } from '../../utils/post';

const RegistrationForm = () => {
  const [first_name, setName] = useState('');
  const [last_name, setSurname] = useState('');
  const [middle_name, setMiddleName] = useState('');
  const [telephone, setTelephone] = useState('');
  const [email, setEmail] = useState('');
  const [birthdate, setDateOfBirth] = useState('');
  const [password, setPassword] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const [birth_country, setbirth_country] = useState('');
  const [birth_city, setbirth_city] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Form validation
    if (!first_name || !last_name || !email || !password || !repeatPassword) {
      alert('Please fill in all fields');
      return;
    }
    
    if (password !== repeatPassword) {
      alert('Passwords do not match. Please try again.');
      return;
    }

    try {
      // Prepare user data
      const userData = {
        email,
        password,
        birthdate,
        birth_country,
        birth_city,
        first_name,
        last_name,
        middle_name,
        telephone
      };

      // Send registration request
      await post(userData);

      // Redirect to login page after successful registration
      navigate('/Login', { state: { from: '/' } });
    } catch (error) {
      console.error('Error during registration:', error);
      alert('Registration failed. Please try again later.');
    }
  };

  return (
    <form className="form-reg" onSubmit={handleSubmit}>
      <div>
        <label htmlFor="name">Имя:</label>
        <input type="text" id="name" value={first_name} onChange={(e) => setName(e.target.value)} />
      </div>
      <div>
        <label htmlFor="Surname">Фамилия:</label>
        <input type="text" id="Surname" value={last_name} onChange={(e) => setSurname(e.target.value)} />
      </div>
      <div>
        <label htmlFor="MiddleName">Отчество:</label>
        <input type="text" id="MiddleName" value={middle_name} onChange={(e) => setMiddleName(e.target.value)} />
      </div>
      <div>
        <label htmlFor="Telephone">Телефон:</label>
        <input type="text" id="Telephone" value={telephone} onChange={(e) => setTelephone(e.target.value)} />
      </div>
      <div>
        <label htmlFor="mail">Почта:</label>
        <input type="text" id="mail" value={email} onChange={(e) => setEmail(e.target.value)} />
      </div>
      <div>
        <label htmlFor="Dateofbirth">Время и дата рождения:</label>
        <input type="text" id="Dateofbirth" value={birthdate} onChange={(e) => setDateOfBirth(e.target.value)} />
      </div>
      <div>
        <label htmlFor="Country">Страна рождения:</label>
        <input type="text" id="Country" value={birth_country} onChange={(e) => setbirth_country(e.target.value)} />
      </div>
      <div>
        <label htmlFor="City">Город:</label>
        <input type="text" id="City" value={birth_city} onChange={(e) => setbirth_city(e.target.value)} />
      </div>
      <div>
        <label htmlFor="password">Пароль:</label>
        <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </div>
      <div>
        <label htmlFor="Rpassword">Повторите пароль:</label>
        <input type="password" id="Rpassword" value={repeatPassword} onChange={(e) => setRepeatPassword(e.target.value)} />
      </div>
      <button type="submit">Зарегистрироваться</button>
    </form>
  );
};

export default RegistrationForm;
