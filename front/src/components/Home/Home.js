import { useNavigate } from 'react-router-dom';
import GHeader from '../Header/header.tsx';
import GFooter from '../Footer/footer.tsx'; 
import Card from '../Card/Card.jsx'


function Home() {
  const navigate = useNavigate();

  return (
    <>
      <GHeader />
      <div>
        <h1>О компании</h1>
        <p>«Наймикс» — компания-разработчик платформы, которая позволяет выстраивать официально-деловые отношения между организациями и лицами, оказывающими услуги в различных сферах деятельности.</p>
      </div>
      <div>
        <Card />
      </div>
      <GFooter />
    </>
  );
}

export default Home;