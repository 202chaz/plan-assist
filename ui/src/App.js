import logo from './logo.svg';
import './App.css';
import PlanValidator from './Plan';
import NavBar from './components/Navbar';

function App() {
  return (
    <div className="App">
      <NavBar />
      <PlanValidator />
    </div>
  );
}

export default App;
