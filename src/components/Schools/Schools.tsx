import React, { useContext, useEffect, useState } from "react";
import { Navigate, useNavigate } from "react-router-dom";
import { mainStyles } from "../../components/AppStyles";
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
  Autocomplete,
  TextField,
} from "@mui/material";
import ImageIcon from "@mui/icons-material/Image";
import SearchIcon from "@mui/icons-material/Search";
import { useGetSchoolsQuery } from "../../redux/apiSlice";
import styles from "./Schools.module.css";


export default function Home() {
  const { data, error, isLoading } = useGetSchoolsQuery("");
  const [valueSearchSchool, setValueSearchSchool] = useState("");
  let navigate = useNavigate();

  const changeValueSearch = (item: React.ChangeEvent<HTMLInputElement>) => {
    setValueSearchSchool(item.target.value);
  };

  const itemIncludes = (item: any) => {
    return item.name
      .trim()
      .toLowerCase()
      .includes(valueSearchSchool.toLowerCase());
  };

  const openRaitingSchool = (item: any) => {
    navigate(`/AthletesRating/${item.id}`, { state: { id: item.id } });
  };


  return (
    <div >
      <div className= {styles.content}>
        <Paper component="form" sx={mainStyles.paperStyles}>
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
      </div>

      {error ? (
        <>Oh no, there was an error</>
      ) : isLoading ? (
        <>Loading...</>
      ) : data ? (
        <List
        >
          {data
            .filter((itemF) => itemIncludes(itemF))
            .map((item) => (
              <div
                style={{ display: "flex", justifyContent: "center" }}
                key={item.id}
              >
                <ListItemButton
                  key={item.id}
                  sx={mainStyles.listItem}
                  onClick={(event) => {
                    openRaitingSchool(item);
                  }}
                >
                  <ListItemAvatar>
                    <Avatar>
                      <ImageIcon />
                    </Avatar>
                  </ListItemAvatar>

                  <div style={{display: "flex", flexDirection: "column"}}>
                    <div
                      style={{
                        color: "black",
                        fontSize: 22,
                      }}
                    >
                      {item.name}
                    </div>

                    <div
                      style={{
                        color: "#7F7F7F",
                        //fontWeight: "bold",
                        fontSize: 12,
                      }}
                    >
                      {item.adress}
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
