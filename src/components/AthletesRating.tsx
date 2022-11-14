import React, { useState, useEffect } from "react";
import {
  Navigate,
  useNavigate,
  useLocation,
  useParams,
} from "react-router-dom";
import { useGetRatingQuery } from "../redux/apiSlice";
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
  TextField,
  Box,
} from "@mui/material";
import { flexbox } from "@mui/system";

import dayjs, { Dayjs } from "dayjs";
import { LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { DatePicker } from "@mui/x-date-pickers/DatePicker";

export default function AthletesRating() {
  let navigate = useNavigate();
  const location = useLocation();
  const state = location.state as CustomizedState; // Type Casting, then you can get the params passed via router
  const { id } = state;

  const [dateStart, setDateStart] = React.useState<Dayjs | null>(dayjs().startOf('year'));
  const [dateEnd, setDateEnd] = React.useState<Dayjs | null>(dayjs().endOf('year'));

  const [dateStartFormat, setDateStartFormat] = React.useState<string>("0001-01-01");
  const [dateEndFormat, setDateEndFormat] = React.useState<string>("0001-01-01");

  const { idS } = useParams<{ idS: string }>();

  // let { idS } = useParams<ParamTypes>();
  console.log(idS);

  useEffect(()=> {
    onChangeStartDate(dateStart);
    onChangeEndDate(dateEnd);
  }, []);

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

  const onChangeStartDate = (newValue: Dayjs|null) => {
    setDateStart(newValue);
    setDateStartFormat(newValue !== null ? newValue?.format('YYYY-MM-DD').toString(): "0001-01-01");
  }

  const onChangeEndDate = (newValue: Dayjs|null) => {
    setDateEnd(newValue);
    setDateEndFormat(newValue !== null ? newValue?.format('YYYY-MM-DD').toString(): "0001-01-01");
  }

  const { data, error, isLoading } = useGetRatingQuery({
    //id: id,
    id: idS !== undefined ? idS : "",
    startDate: dateStartFormat,
    endDate: dateEndFormat,
  });

  console.log(data);  

  const openRatingSportsman = (idS: any, item: any) => {
    console.log(item);

    navigate(`/AthletesRating/${idS}/Sportsman/${item.sportsman.id}/${dateStartFormat}/${dateEndFormat}`, {
      state: { id: item.id },
    });
  };

  return (
    <div style={mainStyles.main}>
      <div
        style={{
          justifyContent: "center",
          display: "flex",
          flexDirection: "row",
          marginTop: "40px",
          marginLeft: "20px",
          marginRight: "20px",
          flex: 1,

          //maxWidth: "600px",
          //alignItems: "center"
        }}
      >
        <LocalizationProvider dateAdapter={AdapterDayjs}>
          <div
            style={
              window.screen.width > 600
                ? {
                    width: "260px",
                    marginRight: "40px",
                    backgroundColor: "white",
                  }
                : {
                    width: "260px",
                    marginRight: "10px",
                    backgroundColor: "white",
                  }
            }
          >
            <DatePicker
              inputFormat="DD.MM.YYYY"
              label="Дата начала"
              value={dateStart}
              onChange={(newValue) => onChangeStartDate(newValue)}
              renderInput={(params) => <TextField {...params} />}
            />
          </div>
          <div
            style={
              window.screen.width > 600
                ? {
                    width: "260px",
                    marginLeft: "40px",
                    backgroundColor: "white",
                  }
                : {
                    width: "260px",
                    marginLeft: "10px",
                    backgroundColor: "white",
                  }
            }
          >
            <DatePicker
              inputFormat="DD.MM.YYYY"
              label="Дата окончания"
              value={dateEnd}
              onChange={(newValue) => {onChangeEndDate(newValue)}}
              renderInput={(params) => <TextField {...params} />}
            />
          </div>
        </LocalizationProvider>
      </div>

      <div style={{ display: "flex", justifyContent: "center" }}>
        <Paper
          component="form"
          sx={{ ...mainStyles.paperStyles, marginTop: "20px" }}
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
              <div
                style={{ display: "flex", justifyContent: "center" }}
                key={item.sportsman.id}
              >
                <ListItemButton
                  key={item.sportsman.id}
                  sx={mainStyles.listItem}
                  onClick={(event) => {
                    openRatingSportsman(idS, item);
                  }}
                >
                  <div style={{ marginLeft: "10px" }}>
                    <Badge badgeContent={item.place} color="primary"></Badge>
                  </div>

                  <div style={{ marginLeft: 20, maxWidth: "200px" }}>
                    <div
                      style={{
                        color: "#7F7F7F",
                        fontWeight: "bold",
                        fontSize: 16,
                      }}
                    >
                      {item.sportsman.name}
                    </div>
                    {/* <ListItemText primary={item.sportsman.name} /> */}
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
    justifyContent: "center",
  },
  points: {
    width: "40px",
    height: "20px",
    backgroundColor: "rgba(220, 230, 218, 1)",
    right: "10px",
    position: "absolute",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
} as const;

interface CustomizedState {
  id: string;
}
interface ParamTypes {
  idS: string;
}
