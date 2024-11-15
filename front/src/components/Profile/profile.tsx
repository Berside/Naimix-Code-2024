import React, { useState } from 'react';
import Gheader from '../Header/header.tsx'
import GFooter from '../Footer/footer.tsx';
const ProfileComponent = () => {
  const [profileInfo, setProfileInfo] = useState({
    name: '',
    email: '',
    bio: ''
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setProfileInfo(prevState => ({ ...prevState, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Профиль обновлен:', profileInfo);
  };

  return (
    <>
    <Gheader />
    <section className="profile-component">
      <h2>Профиль пользователя</h2>
      <form onSubmit={handleSubmit}>
        <div className="profile-info">
          <label htmlFor="name">Имя:</label>
          <input type="text" id="name" name="name" value={profileInfo.name} onChange={handleInputChange} required/>
        </div>
        <div className="profile-info">
          <label htmlFor="email">Email:</label>
          <input type="email" id="email" name="email" value={profileInfo.email} onChange={handleInputChange} required/>
        </div>

        <div className="profile-info">
          <label htmlFor="bio">Описание:</label>
          <textarea id="bio" name="bio" value={profileInfo.bio} onChange={handleInputChange} required> </textarea>
        </div>
        <button type="submit">Сохранить изменения профиль</button>
      </form>
    </section>
    <GFooter/>
    </>
  );
};

export default ProfileComponent;