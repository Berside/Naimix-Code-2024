import LogForm from './components/LogForm/log.tsx'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './hooks/useAuth.js';
import Home from './components/Home/Home.js';
import Reg from './components/RegForm/reg.tsx'

function App() {
  return (
    <Router>
      <AuthProvider>
        <Routes>
          <Route path="/" element={<Reg />} />
          <Route path="/Login" element={<LogForm />} />
          <Route path="/Home" element={<Home />} />
        </Routes>
      </AuthProvider>
    </Router>
  );
}
export default App;
