import React, { useContext, useEffect, useState } from "react";
import {
  Navigate,
  useNavigate,
  useLocation,
  useParams,
} from "react-router-dom";

import Button from '@mui/material/Button';
import Avatar from '@mui/material/Avatar';
import Typography from "@mui/material/Typography";
import styles from "./Header.module.css";
import { Link } from "react-router-dom";

export default function Sportsman() {


  return (

    <div className={styles.header}>

      <div className={styles.headerContent}>

    
        <Typography
            component={Link}
             to={"/"}
            variant="h6"
            color="inherit"
            noWrap
            sx={{ flexGrow: 1, textDecoration: 'none' }}
          >
            SPORTS RATING
          </Typography>
        

        <div>
          <Button onClick={() => window.location.href = 'http://sportsrating.ru:8080/first-line/admin/'}>
            <Avatar src="/broken-image.jpg" />
          </Button>
        </div>

      </div>

    </div>



  );
}

interface CustomizedState {
  id: string;
}
