import "./App.css";
import Drawer from "./components/Drawer";
import { Routes, Route } from "react-router-dom";
import Schools from "./components/Schools";
import Tournament from "./components/Tournament";
// import TournamentСategories from "./components/TournamentСategories";
import AthletesRating from "./components/AthletesRating";

import Sportsman from "./components/Sportsman";


function App() {

  return (
    <>
      <Drawer />
      <Routes>
        <Route path="/" element={<Schools />} />
        <Route path="/AthletesRating/:idS" element={<AthletesRating />} />
        <Route path="/AthletesRating/:idS/Sportsman/:idSp" element={<Sportsman />}/>
        <Route path="/AthletesRating/:idS/Sportsman/:idSp/Tournament/:idT" element={<Tournament />} />
        {/* <Route path="/TournamentСategories" element={<TournamentСategories />}/> */}
      </Routes>
    </>
  );
}

export default App;
