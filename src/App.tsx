import "./App.css";
import Drawer from "./components/Drawer";
import { Routes, Route, Link } from "react-router-dom";
import Schools  from "./components/Schools";
import Tournaments from "./components/Tournaments";
import TournamentСategories from "./components/TournamentСategories";
import AthletesRating from "./components/AthletesRating";
import SignIn from "./components/SignIn";
import SchoolTable from "./components/Administration/SchoolTable";
import SchoolCard from "./components/Administration/SchoolCard";


function App() {
  return (
    <>
      <Drawer />
        <Routes>
          
          <Route path="/" element={<Schools />} />
          <Route path="/AthletesRating" element={<AthletesRating />} />
          
          <Route path="/SchoolTable" element={<SchoolTable />} />
          <Route path="/SchoolTable/:id" element={<SchoolCard />} />

          <Route path="/Tournaments" element={<Tournaments />} />
          <Route path="/SignIn" element={<SignIn />} />
          <Route path="/TournamentСategories" element={<TournamentСategories />}
    />
        </Routes>
    </>
  );
}

export default App;