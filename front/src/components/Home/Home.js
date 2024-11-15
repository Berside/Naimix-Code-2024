import { useNavigate } from 'react-router-dom';
import GHeader from '../Header/header.tsx';
import GFooter from '../Footer/footer.tsx'; 


function Home() {
  const navigate = useNavigate();

  const handleLoginClick = () => {
    console.log('Button clicked');
    navigate('/login');
  };

  return (
    <>
      <GHeader />
      <div>
        <h1>О компании</h1>
        <button onClick={handleLoginClick}>Login</button>
      </div>
      <GFooter />
    </>
  );
}

export default Home;