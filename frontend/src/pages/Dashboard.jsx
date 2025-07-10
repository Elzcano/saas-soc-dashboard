import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";

const Dashboard = () => {
  const { logout } = useContext(AuthContext);

  return (
    <div>
      <h2>Bienvenido al Dashboard</h2>
      <button onClick={logout}>Cerrar sesión</button>
    </div>
  );
};

export default Dashboard;
