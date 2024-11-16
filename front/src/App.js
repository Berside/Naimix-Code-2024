import LogForm from './components/LogForm/log.tsx';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './hooks/useAuth.js';
import Home from './components/Home/Home.js';
import Reg from './components/RegForm/reg.tsx';
import Prof from './components/Profile/profile.tsx';
import Fmain from './components/main/main.tsx'
import CompatibilityForm from './components/Nat_cart/Nat_cart.tsx';

function App() {
  return (
    <Router>
      <AuthProvider>
        <Routes>
          <Route path="/" element={<Reg />} />
          <Route path="/Login" element={<LogForm />} />
          <Route path="/Home" element={<Home />} />
          <Route path="/Profile" element={<Prof />} />
          <Route path="/main" element={<Fmain />} />
          <Route path="/compatibility" element ={<CompatibilityForm/>}/>
        </Routes>
      </AuthProvider>
    </Router>
  );
}
export default App;
