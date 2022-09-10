import "./App.css";
import Drawer from "./components/Drawer";
import { Routes, Route } from "react-router-dom";
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
          <Route path="/AthletesRating/:idS" element={<AthletesRating />} />
          <Route path="/AthletesRating/:idS/Sportsman/:idSp" element={<Sportsman/>} />
          <Route path="/Tournaments" element={<Tournaments />} />
          <Route path="/TournamentСategories" element={<TournamentСategories />}
    />
        </Routes>
    </>
  );
}

export default App;