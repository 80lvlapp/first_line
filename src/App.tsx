
import { Routes, Route } from "react-router-dom";
import Schools from "./components/Schools";
import Tournament from "./components/Tournament";
import AthletesRating from "./components/AthletesRating";
import Sportsman from "./components/Sportsman";
import Header from "./components/Header";

import styles from "./App.module.css";

function App() {

  return (
    <div className={styles.app}>
   {/* <Drawer />*/}
    <Header/>
    
    <div className={styles.content}>
    
        <Routes>
      
          <Route path="/" element={<Schools />} />
          <Route path="/AthletesRating/:idS" element={<AthletesRating />} />
          <Route path="/AthletesRating/:idS/Sportsman/:idSp/:startDate/:endDate" element={<Sportsman />} />
          <Route path="/AthletesRating/:idS/Sportsman/:idSp/:startDate/:endDate/Tournament/:idT" element={<Tournament />} />
        </Routes>
        </div>

        </div>




  );
}

export default App;
