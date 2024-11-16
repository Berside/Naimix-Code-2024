import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './reg.css'

const RegistrationForm = () => {
  const [name, setname] = useState('');
  const [Surname, setSurname] = useState('');
  const [MiddleName, setMiddleName] = useState('');
  const [Telephone, setTelephone] = useState('');
  const [mail, setmail] = useState('');
  const [Dateofbirth, setDateofbirth] = useState('');
  const [Rpassword, setRpassword] = useState('');
  const [password, setPassword] = useState('');
  const [Country, setCountry] = useState('');
  const [City, setCity] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async(e) => {
    e.preventDefault();
    console.log('Форма отправлена:', { name, Surname, MiddleName, Telephone,  mail, Dateofbirth, password, Rpassword});
    if (password !== Rpassword) {
        alert('Пароли не совпадают. Пожалуйста, повторите попытку.');
        return;
    }
    try {
        const userData = {
          name,
          Surname,
          MiddleName,
          Telephone,
          mail,
          Dateofbirth,
          password
        };
        navigate('/Login', { state: { from: '/' } });
    } catch (error) {
      console.error('Ошибка при регистрации:', error);
      alert('Произошла ошибка при регистрации. Пожалуйста, попробуйте снова.');
    }
  };
  return (
    <form className = 'form-reg' onSubmit={handleSubmit}>
      <div>
        <label htmlFor="name">Имя:</label>
        <input type="text" id="name" value={name} onChange={(e) => setname(e.target.value)} />
      </div>
      <div>
        <label htmlFor="Surname">Фамилия:</label>
        <input type="text" id="Surname" value={Surname} onChange={(e) => setSurname(e.target.value)} />
      </div>
      <div>
        <label htmlFor="MiddleName">Отчество:</label>
        <input type="text" id="MiddleName" value={MiddleName} onChange={(e) => setMiddleName(e.target.value)} />
      </div>
      <div>
        <label htmlFor="Telephone">Телефон:</label>
        <input type="text" id="Telephone" value={Telephone} onChange={(e) => setTelephone(e.target.value)} />
      </div>
      <div>
        <label htmlFor="mail">Почта:</label>
        <input type="text" id="mail" value={mail} onChange={(e) => setmail(e.target.value)} />
      </div>
      <div>
        <label htmlFor="Dateofbirth">Время и дата рождения:</label>
        <input type="text" id="Dateofbirth" value={Dateofbirth} onChange={(e) => setDateofbirth(e.target.value)} />
      </div>
      <div>
        <label htmlFor="Country">Страна рождения:</label>
        <input type="text" id="Country" value={Country} onChange={(e) => setCountry(e.target.value)} />
      </div>
      <div>
        <label htmlFor="City">Город:</label>
        <input type="text" id="City" value={City} onChange={(e) => setCity(e.target.value)} />
      </div>
      <div>
        <label htmlFor="password">Пароль:</label>
        <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </div>
      <div>
        <label htmlFor="Rpassword">Повторите пароль:</label>
        <input type="password" id="Rpassword" value={Rpassword} onChange={(e) => setRpassword(e.target.value)} />
      </div>
      <button type="submit">Зарегистрироваться</button>
    </form>
  );
};

export default RegistrationForm;