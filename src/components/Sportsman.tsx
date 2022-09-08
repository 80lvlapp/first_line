import React, { useContext, useEffect, useState } from "react";
import { Navigate, useNavigate, useLocation } from "react-router-dom";
import { useGetRaitingSportsmanQuery } from "../redux/apiSlice";
import { mainStyles } from "../components/AppStyles";
import {
  ListItemButton,
  List,
  ListItemText,
} from "@mui/material";

export default function Sportsman() {
  const location = useLocation();
  const state = location.state as CustomizedState; // Type Casting, then you can get the params passed via router
  const { id } = state;

  // const [valueSearchSportsman, setvalueSearchSportsman] = useState("");

  // const changeValueSearch = (item: React.ChangeEvent<HTMLInputElement>) => {
  //   setvalueSearchSportsman(item.target.value);
  // };

  const itemIncludes = (item: any) => {
    return true;
    // return item.sportsman.name
    //   .trim()
    //   .toLowerCase()
    //   .includes(valueSearchSportsman.toLowerCase());
  };

  const { data, error, isLoading } = useGetRaitingSportsmanQuery({
    id: id,
    startDate: "2022",
    endDate: "2022",
  });

  console.log(data);

  return (
    <div style={mainStyles.main}>
      {/* <div style={{ display: "flex", justifyContent: "center" }}>
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
        </div> */}

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
          {data.tournaments
            .filter((itemF) => itemIncludes(itemF))
            .map((item) => (
              <div style={{ display: "flex", justifyContent: "center" }}>
                <ListItemButton
                  key={item.tournament.id}
                  sx={mainStyles.listItem}
                  onClick={(event) => {
                    // openRaitingSchool(item);
                  }}
                >
                  <div style={{ marginLeft: 20, maxWidth: "200px" }}>
                    <ListItemText primary={item.tournament.name} />
                  </div>
                </ListItemButton>
              </div>
            ))}
        </List>
      ) : null}
    </div>
  );
}

interface CustomizedState {
  id: string;
}
