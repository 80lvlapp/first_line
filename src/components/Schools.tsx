//import React, { useContext, useEffect } from "react";
//import { useAppContext } from "../context/AppContext";
import { List } from "@mui/material";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import ListItemAvatar from "@mui/material/ListItemAvatar";
import Avatar from "@mui/material/Avatar";
import ImageIcon from "@mui/icons-material/Image";
import { RootState } from '../redux/store'
import { useSelector} from 'react-redux'

export default function Home() {
  
  //const { state, changeState, testChangeState, getSportsSchools } =
    //useAppContext();

  //useEffect(() => {
    //getSportsSchools();
  //}, []);

  const schools = useSelector((state: RootState) => state.schools.value)

  //const onClickButton = () => {
    // changeState({type: ActionType.CHANGE, payload: "test"});
    //testChangeState("yeeeee");
    //alert(state.stringParam);
    //console.log(state);
  //};

  return (
    <div style={{marginTop: 1}}>
      {/* <h4>Стартовая страница</h4>
      <button type="submit" onClick={() => onClickButton()}>
        Тест редюсер
      </button> */}
      <List sx={{ width: "100%", maxWidth: 360, bgcolor: "background.paper", marginTop: 0 }}>
        {schools.map((item) => (
          <ListItem key={item.id}>
            <ListItemAvatar>
              <Avatar>
                <ImageIcon />
              </Avatar>
            </ListItemAvatar>
            <ListItemText primary= {item.name} secondary= {item.adress} />
          </ListItem>
        ))}
      </List>
    </div>
  );
}
