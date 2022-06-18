import React, { useContext, useEffect, useState } from "react";
import {Navigate, useNavigate} from 'react-router-dom';
import {Styles} from '../components/AppStyles';
//import { useAppContext } from "../context/AppContext";
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
import ImageIcon from "@mui/icons-material/Image";
import SearchIcon from "@mui/icons-material/Search";
import { useGetSchoolsQuery } from "../redux/apiSlice";

export default function Home() {
  const { data, error, isLoading } = useGetSchoolsQuery("");
  const [valueSearchSchool, setValueSearchSchool] = useState("");
  let navigate = useNavigate();

  const changeValueSearch = (item: React.ChangeEvent<HTMLInputElement>) => {
    setValueSearchSchool(item.target.value);
  };

  const itemIncludes = (item: any) => {
    return item.name.trim().toLowerCase().includes(valueSearchSchool);
  };

  const openRaitingSchool = (item: any) => {
    console.log(item);

    navigate("/AthletesRating", { state: { id: item.id } });
  
  }

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
          placeholder="Поиск школы"
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
                key={item.id}
                sx={{
                  marginLeft: "20px",
                  marginTop: "10px",
                  background: "#FFFFFF",
                  borderRadius: "10px",
                }}
                onClick = {(event) => {openRaitingSchool(item)}}
              >
                <ListItemAvatar>
                  <Avatar>
                    <ImageIcon />
                  </Avatar>
                </ListItemAvatar>
                <ListItemText primary={item.name} secondary={item.adress} />
              </ListItemButton>
            ))}
        </List>
      ) : null}
    </div>
  );
}
