import React, { useState } from "react";
import { Navigate, useNavigate, useLocation, useParams } from "react-router-dom";
import { useGetRaitingQuery } from "../redux/apiSlice";
import ImageIcon from "@mui/icons-material/Image";
import SearchIcon from "@mui/icons-material/Search";
import { mainStyles } from "../components/AppStyles";
import MailIcon from "@mui/icons-material/Image";
import CircleIcon from "@mui/icons-material/Circle";

import {
  InputBase,
  ListItem,
  ListItemButton,
  List,
  ListItemText,
  ListItemAvatar,
  Avatar,
  Paper,
  IconButton,
  Badge,
} from "@mui/material";
import { flexbox } from "@mui/system";

export default function AthletesRating() {
  let navigate = useNavigate();
  const location = useLocation();
  const state = location.state as CustomizedState; // Type Casting, then you can get the params passed via router
  const { id } = state;

  const [valueSearchSportsman, setvalueSearchSportsman] = useState("");

  const changeValueSearch = (item: React.ChangeEvent<HTMLInputElement>) => {
    setvalueSearchSportsman(item.target.value);
  };

  const itemIncludes = (item: any) => {
    return item.sportsman.name
      .trim()
      .toLowerCase()
      .includes(valueSearchSportsman.toLowerCase());
  };

  const { data, error, isLoading } = useGetRaitingQuery({
    id: id,
    startDate: "2022",
    endDate: "2022",
  });

  const openRaitingSportsman = (idS:any, item: any) => {

    console.log(item);

    navigate(`/AthletesRating/${idS}/Sportsman/${item.sportsman.id}`, { state: { id: item.id } });
  };

  const { idS } = useParams<{ idS: any }>();

  return (
    <div
      style={mainStyles.main}>
      <div style={{ display: "flex", justifyContent: "center" }}>
        <Paper component="form" sx={{ ...mainStyles.paperStyles }}>
          <InputBase
            sx={{ ml: 1, flex: 1 }}
            placeholder="Поиск спортсмена"
            // value = {valueSearchSchool}
            onChange={changeValueSearch}
            inputProps={{ "aria-label": "search google maps" }}
          />
          <IconButton
            type="submit"
            sx={{ p: "10px" }}
            aria-label="search"
            disabled={true}
          >
            <SearchIcon />
          </IconButton>
        </Paper>
      </div>

      {error ? (
        <>Oh no, there was an error</>
      ) : isLoading ? (
        <>Loading...</>
      ) : data ? (
        <List
          sx={{
            background: "#E5E5E5",
            marginTop: 1,
            marginRight: "20px",
          }}
        >
          {data
            .filter((itemF) => itemIncludes(itemF))
            .map((item) => (
              <div style={{ display: "flex", justifyContent: "center" }}>
                <ListItemButton
                  key={item.sportsman.id}
                  sx={mainStyles.listItem}
                  onClick={(event) => {
                    openRaitingSportsman(idS, item);
                  }}
                >
                  <div>
                    <Badge badgeContent={item.place} color="primary"></Badge>
                  </div>

                  <div style={{ marginLeft: 20, maxWidth: "200px" }}>
                    <ListItemText primary={item.sportsman.name} />
                  </div>

                  <div style={styles.containerTriangle}>
                    <div
                      style={
                        item.сhangingPosition === 0
                          ? {}
                          : item.сhangingPosition > 0
                            ? { ...styles.triangle, ...styles.arrowUp }
                            : { ...styles.triangle, ...styles.arrowDown }
                      }
                    />

                    <div
                      style={{
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "flex-end",
                      }}
                    >
                      <span>{item.сhangingPosition}</span>
                    </div>
                    {/* <div> {item.сhangingPosition} </div> */}
                  </div>

                  <div style={styles.points}>
                    <div
                      style={{
                        display: "flex",
                        alignItems: "center",
                        // position: "relative",
                        justifyContent: "center",
                      }}
                    >
                      <span>{item.points}</span>
                    </div>
                  </div>
                </ListItemButton>
              </div>
            ))}
        </List>
      ) : null}
    </div>
  );
}

const styles = {
  triangle: {
    width: 0,
    height: 0,
    backgroundColor: "transparent",
    borderStyle: "solid",
    marginTop: "0px",
  },
  arrowUp: {
    borderTopWidth: 0,
    borderRightWidth: 10,
    borderBottomWidth: 10,
    borderLeftWidth: 10,
    borderTopColor: "transparent",
    borderRightColor: "transparent",
    borderBottomColor: "#007F00",
    borderLeftColor: "transparent",
  },
  arrowDown: {
    borderTopWidth: 0,
    borderRightWidth: 10,
    borderBottomWidth: 10,
    borderLeftWidth: 10,
    borderTopColor: "transparent",
    borderRightColor: "transparent",
    borderBottomColor: "tomato",
    borderLeftColor: "transparent",
  },
  containerTriangle: {
    width: "40px",
    height: "20px",
    backgroundColor: "rgba(220, 230, 218, 1)",
    //marginLeft: "250px",
    right: "70px",
    position: "absolute",
    display: "flex",
    alignItems: "center",
    justifyContent: "flex-end",
  },
  points: {
    width: "40px",
    height: "20px",
    backgroundColor: "rgba(220, 230, 218, 1)",
    right: "10px",
    position: "absolute",
    display: "flex",
    //alignItems: "flex-end",
    justifyContent: "flex-end"
  },
} as const;

interface CustomizedState {
  id: string;
}
