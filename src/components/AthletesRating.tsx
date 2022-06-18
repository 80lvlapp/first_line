import React, {useState} from "react";
import { Navigate, useNavigate, useLocation } from "react-router-dom";
import { useGetRaitingQuery } from "../redux/apiSlice";
import ImageIcon from "@mui/icons-material/Image";
import SearchIcon from "@mui/icons-material/Search";
import {Styles} from '../components/AppStyles';

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
} from "@mui/material";

export default function AthletesRating() {
  
  const location = useLocation();
  const state = location.state as CustomizedState; // Type Casting, then you can get the params passed via router
  const { id } = state;

  const [valueSearchSportsman, setvalueSearchSportsman] = useState("");

  const changeValueSearch = (item: React.ChangeEvent<HTMLInputElement>) => {
    setvalueSearchSportsman(item.target.value);
  };

  const itemIncludes = (item: any) => {
    return item.sportsman.name.trim().toLowerCase().includes(valueSearchSportsman.toLowerCase());
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
      <Paper
        component="form"
        sx={Styles.paperStyles}
      >
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
              <ListItemButton
                key={item.sportsman.id}
                sx={{
                  marginLeft: "20px",
                  marginTop: "10px",
                  background: "#FFFFFF",
                  borderRadius: "10px",
                }}
                onClick={(event) => {
                  // openRaitingSchool(item);
                }}
              >
                <ListItemAvatar>
                  <Avatar>
                    <ImageIcon />
                  </Avatar>
                </ListItemAvatar>
                <ListItemText primary={item.sportsman.name}/>
              </ListItemButton>
            ))}
        </List>
      ) : null}
    </div>
  );
}

interface CustomizedState {
  id: string;
}
