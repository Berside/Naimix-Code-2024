import React, { createContext, useContext, useState } from 'react';
import { useNavigate } from 'react-router-dom';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const navigate = useNavigate();

  const login = () => {
    setIsAuthenticated(true);
    navigate('/Reg');
  };

  const logout = () => {
    setIsAuthenticated(false);
    navigate('/');
  };
  const Home = () => {
    setIsAuthenticated(false);
    navigate('/Home');
  };
  const main = () => {
    setIsAuthenticated(false);
    navigate('/Main');
  };
  

  const value = {
    isAuthenticated,
    login,
    logout,
    Home,
    main
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};
export const useAuth = () => useContext(AuthContext);
