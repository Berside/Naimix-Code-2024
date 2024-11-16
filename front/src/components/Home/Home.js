import { useNavigate } from 'react-router-dom';
import GHeader from '../Header/header.tsx';
import GFooter from '../Footer/footer.tsx';
import Card from '../Card/Card.jsx';
import './home.css';

function Home() {
  const navigate = useNavigate();

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
            <Card title="Сотрудник 1" onClick={() => navigate('/catalog/1')} />
            <Card title="Сотрудники 2" onClick={() => navigate('/catalog/2')} />
            <Card title="Сотрудники 3" onClick={() => navigate('/catalog/3')} />
          </div>
          <button className="catalog-button" onClick={() => navigate('/catalog')}>Перейти в каталог</button>
        </section>
      </div>
      <GFooter />
    </>
  );
}

export default Home;