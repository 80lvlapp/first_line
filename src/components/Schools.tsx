import React, { useContext, useEffect } from "react";
//import { useAppContext } from "../context/AppContext";
import {
  InputBase,
  ListItem,
  List,
  ListItemText,
  ListItemAvatar,
  Avatar,
  Paper,
  IconButton
} from "@mui/material";
import ImageIcon from "@mui/icons-material/Image";
import SearchIcon from '@mui/icons-material/Search';
import { useGetSchoolsQuery } from "../redux/apiSlice";

export default function Home() {
  const { data, error, isLoading } = useGetSchoolsQuery("");
  return (
    <div style={{ flex: 1, marginTop: 0, background: "#E5E5E5", height: "100vh",  overflow: "hidden" }}>
      
      <Paper
         component="form"
        sx={{
          p: "2px 4px",
          display: "flex",
          alignItems: "center",
          width: "100%",
          maxWidth: 360,
          marginTop: "40px",
          marginLeft: "20px",
        }}
      >
        <InputBase
          sx={{ ml: 1, flex: 1 }}
          placeholder="Поиск школы"
          // inputProps={{ "aria-label": "search google maps" }}
        />
        <IconButton type="submit" sx={{ p: "10px" }} aria-label="search">
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
            // width: "100%",
            // maxWidth: 360,
            // bgcolor: "background.paper",
            background: "#E5E5E5",
            marginTop: 1,
            marginRight: "50px"
          }}
        >
          {data.map((item) => (
            <ListItem key={item.id} sx = {{
              // position: 'absolute',
              // width: "320px",
              // height: "60px",
              marginLeft: "20px",
              
               marginTop: "10px",
               background: "#FFFFFF",
              borderRadius: "10px"
              }}>
              <ListItemAvatar>
                <Avatar>
                  <ImageIcon />
                </Avatar>
              </ListItemAvatar>
              <ListItemText primary={item.name} secondary={item.adress} />
            </ListItem>
          ))}
        </List>
      ) : null}
    </div>
  );
}
