import React, { useState } from "react";
import { Navigate, useNavigate, useLocation } from "react-router-dom";
import { useGetRaitingQuery } from "../redux/apiSlice";
import ImageIcon from "@mui/icons-material/Image";
import SearchIcon from "@mui/icons-material/Search";
import { Styles } from "../components/AppStyles";
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

  console.log(data);

  return (
    <div
      style={{
        flex: 1,
        marginTop: 0,
        background: "#E5E5E5",
        height: "100vh",
        overflow: "hidden",
      }}
    >
      <div style={{ display: "flex", justifyContent: "center" }}>
        <Paper component="form" sx={{...Styles.paperStyles}}>
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
                  sx={{
                    marginLeft: "20px",
                    marginTop: "10px",
                    background: "#FFFFFF",
                    borderRadius: "10px",
                    maxWidth: "600px",
                  }}
                  onClick={(event) => {
                    // openRaitingSchool(item);
                  }}
                >
                  <div>
                    <Badge badgeContent={item.place} color="primary"></Badge>
                  </div>
                  {/* <ListItemAvatar>
                  <Avatar>
                    <ImageIcon />
                  </Avatar>
                </ListItemAvatar> */}
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
                        justifyContent: "center",
                      }}
                    >
                      <span>{item.сhangingPosition}</span>
                    </div>
                    {/* <div> {item.сhangingPosition} </div> */}
                  </div>

                  <div
                    style={{
                      width: "40px",
                      height: "20px",
                      backgroundColor: "rgba(220, 230, 218, 1)",
                      marginLeft: "300px",
                      position: "absolute",
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center",
                    }}
                  >
                    <div
                      style={{
                        display: "flex",
                        alignItems: "center",
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
    marginLeft: "250px",
    position: "absolute",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
} as const;

interface CustomizedState {
  id: string;
}
