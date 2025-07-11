import { useContext, useState } from "react";
import axios from "axios";
import { AuthContext } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

const Login = () => {
  // Obtenemos la función login desde el contexto
  const { login } = useContext(AuthContext);

  // Estado para almacenar los datos del formulario
  const [form, setForm] = useState({ username: "", password: "" });

  // Hook para redirigir al usuario después del login
  const navigate = useNavigate();

  // Manejador de cambios en los inputs del formulario
  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // Manejador del envío del formulario
  const handleSubmit = async (e) => {
    e.preventDefault(); // Evita que la página se recargue

    try {
      // Enviamos los datos como JSON al backend
      const res = await axios.post("http://127.0.0.1:8000/login", form, {
        headers: {
          "Content-Type": "application/json", // 👈 Indica que enviamos JSON
        },
      });

      // Guardamos el token en el contexto (o localStorage si así lo configuras)
      login(res.data.access_token);

      // Redirigimos al dashboard después del login exitoso
      navigate("/dashboard");
    } catch (err) {
      // Mostramos error si el login falla
      alert("Credenciales incorrectas");
      console.error(err.response?.data || err.message); // Opcional: ver detalles en consola
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input
          name="username"
          placeholder="Usuario"
          onChange={handleChange}
          value={form.username}
        />
        <input
          name="password"
          type="password"
          placeholder="Contraseña"
          onChange={handleChange}
          value={form.password}
        />
        <button type="submit">Iniciar sesión</button>
      </form>
    </div>
  );
};

export default Login;

