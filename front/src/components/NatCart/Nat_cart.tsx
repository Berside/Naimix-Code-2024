import React from "react";
import "./nat_cart.css";
import GHeader from "../Header/header.tsx";
import GFooter from "../Footer/footer.tsx";

const CompatibilityForm = () => {
  const handleCalculate = (event) => {
    event.preventDefault();
    console.log("Рассчитываем совместимость сотрудников...");
  };

  return (
    <div>
      <GHeader />
      <div className="compatibility-container">
        <h1 className="title">Совместимость сотрудников</h1>
        <form className="form-container" onSubmit={handleCalculate}>
          <label>
            Сотрудник 1
            <input type="text" placeholder="Введите имя сотрудника 1" required />
          </label>
          <label>
            Дата рождения 1 сотрудника
            <input type="date" required />
          </label>
          <label>
            Сотрудник 2
            <input type="text" placeholder="Введите имя сотрудника 2" required />
          </label>
          <label>
            Дата рождения 2 сотрудника
            <input type="date" required />
          </label>
          <button type="submit">Рассчитать</button>
        </form>
        <div className="diagram-placeholder">
          Диаграмма будет отображаться здесь
        </div>
      </div>
      <GFooter />
    </div>
  );
};

export default CompatibilityForm;
