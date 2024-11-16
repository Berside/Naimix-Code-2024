import { useNavigate } from 'react-router-dom';
import GHeader from '../Header/header.tsx';
import GFooter from '../Footer/footer.tsx';
import Card from '../Card/Card.jsx';
import './home.css';
import {CheckStatus} from '../../utils/CheckStatus.jsx'
function Home() {
  const navigate = useNavigate();

  const handleCheckStatus = async () => {
    try {
      const result = await CheckStatus();
      console.log('Результат проверки статуса:', result);
    } catch (error) {
      console.error('Произошла ошибка:', error);
    }
    fetch("0.0.0.0:7000/api/v1/auth/status/").then(res => {
      if (res.ok) {
      res.json().then(data => console.log(data));
      }
      })
  };

  return (
    <>
      <GHeader />
      <div className="home-container">
        <section className="about-section">
          <div className="about-text">
            <h1>О компании</h1>
            <p>
               <strong>«Наймикс»</strong> — компания-разработчик платформы,<br />
                 которая позволяет выстраивать<br />
                  официально-деловые отношения между<br />
                организациями и лицами, оказывающими услуги<br />
                в различных сферах деятельности.
            </p>
          </div>
          <div className="about-image">
            <div className="circle"></div>
          </div>
        </section>
        <section className="compatibility-section">
          <h2>Совместимость сотрудников</h2>
          <div className="cards-container">
            <Card title="Сотрудник 1" onClick={() => navigate('/Main')} />
            <Card title="Сотрудники 2" onClick={() => navigate('/Main')} />
            <Card title="Сотрудники 3" onClick={() => navigate('/Main')} />
          </div>
          <button className="catalog-button" onClick={() => navigate('/compatibility')}>Перейти к поиску</button>
        </section>
      </div>
      <GFooter />
    </>
  );
}

export default Home;