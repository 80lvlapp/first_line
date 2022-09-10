import "./App.css";
import Drawer from "./components/Drawer";
import { Routes, Route, Link } from "react-router-dom";
import Schools  from "./components/Schools";
import Tournaments from "./components/Tournaments";
import TournamentСategories from "./components/TournamentСategories";
import AthletesRating from "./components/AthletesRating";

import Sportsman from "./components/Sportsman";


function App() {
  return (
    <>
      <Drawer />
        <Routes>
          
          <Route path="/" element={<Schools />} />
          <Route path="/AthletesRating" element={<AthletesRating />} />
          <Route path="/Sportsman" element={<Sportsman/>} />
          
        

          <Route path="/Tournaments" element={<Tournaments />} />

          <Route path="/TournamentСategories" element={<TournamentСategories />}
    />
        </Routes>
    </>
  );
}

export default App;