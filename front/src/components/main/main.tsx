import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Lmain = () => {
  const navigate = useNavigate();
  const handleProfileClickReg = (event) => {
    event.preventDefault();
    navigate('/');
};
  return (
    <form>
      <h2>Вход в систему</h2>
      <div>
        </div>
      <button type="submit">Рассчитать</button>
    </form>
  );
};
export default Lmain;
