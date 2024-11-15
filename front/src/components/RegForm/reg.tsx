import React, { useState } from 'react';

const RegistrationForm = () => {
  const [name, setname] = useState('');
  const [Surname, setSurname] = useState('');
  const [MiddleName, setMiddleName] = useState('');
  const [Telephone, setTelephone] = useState('');
  const [mail, setmail] = useState('');
  const [Dateofbirth, setDateofbirth] = useState('');
  const [Rpassword, setRpassword] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Форма отправлена:', { name, Surname, MiddleName, Telephone,  mail, Dateofbirth, password, Rpassword});
  };

  return (
    <form onSubmit={handleSubmit}>
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