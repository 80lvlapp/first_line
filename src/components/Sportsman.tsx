import React, { useContext, useEffect, useState } from "react";
import {
  Navigate,
  useNavigate,
  useLocation,
  useParams,
} from "react-router-dom";
import { useGetRatingSportsmanQuery } from "../redux/apiSlice";
import { mainStyles } from "../components/AppStyles";
import { ListItemButton, List, ListItemText } from "@mui/material";
import { keyboard } from "@testing-library/user-event/dist/keyboard";

export default function Sportsman() {
  const location = useLocation();
  let navigate = useNavigate();
  const state = location.state as CustomizedState; // Type Casting, then you can get the params passed via router
  const { id } = state;
  const { idSp, idS } = useParams<{ idSp: string; idS: string }>();

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

  const { data, error, isLoading } = useGetRatingSportsmanQuery({
    id: idSp !== undefined ? idSp : "",
    startDate: "2022",
    endDate: "2022",
  });

  const openTournament = (item: any) => {
    console.log(item);

    navigate(
      `/AthletesRating/${idS}/Sportsman/${idSp}/Tournament/${item.tournament.id}`,
      {
        state: { id: item.id },
      }
    );
  };

  console.log(data?.sportsman.name);

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
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          paddingLeft: "20px",
          paddingRight: "20px",
        }}
      >
        <div
          style={{
            maxWidth: "600px",
            minHeight: "70px",
            display: "flex",
            justifyContent: "center",
            width: "100%",
          }}
        >
          <div
            style={{
              marginTop: "50px",
              background: "#FFFFFF",
              borderRadius: "10px",
              width: "70%",
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <div
              style={{
                marginTop: "20px",
                marginBottom: "20px",
                marginLeft: 10,
                marginRight: 10,
                color: "#625D8E",
                fontFamily: "inherit",
                fontSize: 21,
                fontWeight: "bold",
              }}
            >
              {data?.sportsman.name}
            </div>
          </div>
          <div
            style={{
              marginLeft: "10px",
              marginTop: "50px",
              background: "#FFFFFF",
              borderRadius: "10px",
              width: "30%",
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <div
              style={{
                marginTop: "20px",
                marginBottom: "20px",
                marginLeft: 10,
                marginRight: 10,
                color: "#625D8E",
                fontFamily: "inherit",
                fontSize: 16,
                fontWeight: "bold",
              }}
            >
              {data?.place} место {"\n"} {data?.points} очков
            </div>
          </div>
        </div>
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
          {data.tournaments
            .filter((itemF) => itemIncludes(itemF))
            .map((item) => (
              <div
                style={{ display: "flex", justifyContent: "center" }}
                key={item.tournament.id}
              >
                <ListItemButton
                  key={item.tournament.id}
                  sx={mainStyles.listItem}
                  onClick={(event) => {
                    openTournament(item);
                  }}
                >
                  <div
                    style={{
                      display: "flex",
                      flexDirection: "row",
                      alignItems: "center",
                    }}
                  >
                    <div
                      style={{
                        color: "#719A70",
                        fontWeight: "bold",
                        fontSize: 15,
                      }}
                    >
                      {item.tournament.date}
                    </div>
                    <div
                      style={{
                        display: "flex",
                        flexDirection: "column",
                        justifyContent: "center",
                        marginLeft: "20px",
                      }}
                    >
                      <div
                        style={{
                          color: "#625D8E",
                          fontWeight: "bold",
                          fontSize: 17,
                        }}
                      >
                        {item.tournament.name}
                      </div>
                      <div style={{ color: "#7F7F7F", fontSize: 12 }}>
                        {item.tournament.venue}
                      </div>
                      <div
                        style={{
                          color: "#7F7F7F",
                          fontWeight: "bold",
                          fontSize: 12,
                        }}
                      >
                        Всего очков: {item.points}
                      </div>
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

interface CustomizedState {
  id: string;
}
