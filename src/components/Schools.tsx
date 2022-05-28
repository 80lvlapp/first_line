//import React, { useContext, useEffect } from "react";
//import { useAppContext } from "../context/AppContext";
import { List } from "@mui/material";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import ListItemAvatar from "@mui/material/ListItemAvatar";
import Avatar from "@mui/material/Avatar";
import ImageIcon from "@mui/icons-material/Image";
import { useGetSchoolsQuery } from '../redux/apiSlice'

export default function Home() {
  const {data, error, isLoading } = useGetSchoolsQuery("");
  return (
    <div style={{ marginTop: 1 }}>

      {error ? (
        <>Oh no, there was an error</>
      ) : isLoading ? (
        <>Loading...</>
      ) : data ? (
        <List sx={{ width: "100%", maxWidth: 360, bgcolor: "background.paper", marginTop: 0 }}>
          {
            data.map((item) => (
              <ListItem key={item.id}>
                <ListItemAvatar>
                  <Avatar>
                    <ImageIcon />
                  </Avatar>
                </ListItemAvatar>
                <ListItemText primary={item.name} secondary={item.adress} />
              </ListItem>
            ))

          }

        </List>
      ) : null}
    </div>
  );
}
