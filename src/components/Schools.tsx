import React, { useContext, useEffect, useState } from "react";
import { Navigate, useNavigate } from "react-router-dom";
import { mainStyles } from "../components/AppStyles";
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
  TextField
} from "@mui/material";
import ImageIcon from "@mui/icons-material/Image";
import SearchIcon from "@mui/icons-material/Search";
import { useGetSchoolsQuery } from "../redux/apiSlice";

export default function Home() {
  
  const { data, error, isLoading } = useGetSchoolsQuery("");
  const [valueSearchSchool, setValueSearchSchool] = useState("");
  let navigate = useNavigate();

  const [yearArray, setYearArray] = useState<number[]>([]);

  useEffect(() => {
    
    let yArray = [];
    yArray.push(2021);
    yArray.push(2022);
    yArray.push(2022);

    setYearArray(yArray);

  }, []);

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
    <div style={mainStyles.main}>
      <div style={{ display: "flex", justifyContent: "center" }}>
        <Paper component="form" sx={mainStyles.paperStyles}>
          <Autocomplete
            disablePortal
            id="combo-box-demo"
            options={yearArray}
            sx={{ width: 300 }}
            renderInput={(params) => <TextField {...params} label="Movie" />}
          />
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
                  <ListItemText primary={item.name} secondary={item.adress} />
                </ListItemButton>
              </div>
            ))}
        </List>
      ) : null}
    </div>
  );
}
