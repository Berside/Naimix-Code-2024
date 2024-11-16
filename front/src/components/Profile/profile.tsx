import React, { useState, useEffect } from 'react';
import Gheader from '../Header/header.tsx';
import GFooter from '../Footer/footer.tsx';
import { useNavigate } from 'react-router-dom';
import './profile.css';

const ProfileComponent = () => {
  const [profileInfo, setProfileInfo] = useState({
    name: '',
    surname: '',
    phone: '',
    email: '',
    middleName: '',
    dateOfBirth: '',
    country: '',
    city: '',
    password: '',
    rPassword: ''
  });
  const navigate = useNavigate();

  useEffect(() => {
    // Populate initial values if available
    // This should be replaced with actual data fetching logic
    setProfileInfo({
      name: 'Илья',
      surname: 'Поверинов',
      phone: '78988983066',
      email: 'babka@mail.ru',
      middleName: 'Владимирович',
      dateOfBirth: '2024-06-09',
      country: 'Russia',
      city: 'Moscow',
      password: '',
      rPassword: ''
    });
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setProfileInfo(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Профиль обновлен:', profileInfo);
    // Add your submission logic here
  };

  const handleProfileClickExit = (event) => {
    event.preventDefault();
    navigate('/Login');
  };

  return (
    <>
      <Gheader />
      <section className="profile-component">
        <h1>Профиль</h1>
        <div className="profile-container">
          <div className="profile-left">
            <form className='form-prof' onSubmit={handleSubmit}>
              <input
                type="text"
                id="name"
                name="name"
                placeholder="Имя"
                value={profileInfo.name}
                onChange={handleInputChange}
                required
              />
              <input
                type="text"
                id="surname"
                name="surname"
                placeholder="Фамилия"
                value={profileInfo.surname}
                onChange={handleInputChange}
                required
              />
              <input
                type="text"
                id="phone"
                name="phone"
                placeholder="Номер телефона"
                value={profileInfo.phone}
                onChange={handleInputChange}
                required
              />
              <input
                type="text"
                id="middleName"
                name="middleName"
                placeholder="Отчество"
                value={profileInfo.middleName}
                onChange={handleInputChange}
                required
              />
              <input
                type="date"
                id="dateOfBirth"
                name="dateOfBirth"
                placeholder="Дата рождения"
                value={profileInfo.dateOfBirth}
                onChange={handleInputChange}
                required
              />
              <input
                type="text"
                id="country"
                name="country"
                placeholder="Страна"
                value={profileInfo.country}
                onChange={handleInputChange}
                required
              />
              <input
                type="text"
                id="city"
                name="city"
                placeholder="Город"
                value={profileInfo.city}
                onChange={handleInputChange}
                required
              />   
              <button type="submit" className="save-button">
                Сохранить
              </button>
            </form>
          </div>
          <div className="profile-right">
            <div className="profile-section">
              <h2>Должность</h2>
              <p>Информация о должности</p>
            </div>
            <div className="profile-section">
              <h2>Совместимость</h2>
              <p>Информация о совместимости</p>
            </div>
          </div>
        </div>
        <button className="exit-button" onClick={handleProfileClickExit}>
          Выйти
        </button>
      </section>
      <GFooter />
    </>
  );
};

export default ProfileComponent;
