import React, { useContext, useEffect, useState } from "react";
import {
  Navigate,
  useNavigate,
  useLocation,
  useParams,
} from "react-router-dom";
import { useGetRatingTournamentQuery } from "../redux/apiSlice";
import { mainStyles } from "../components/AppStyles";
import { ListItemButton, List, ListItemText } from "@mui/material";

export default function Tournament() {
  const { idSp, idT } = useParams<{ idSp: string; idT: string }>();

  const { data, error, isLoading } = useGetRatingTournamentQuery({
    id: idSp !== undefined ? idSp : "",
    idTournament: idT !== undefined ? idT : "",
  });

  const itemIncludes = (item: any) => {
    return true;
  };

  console.log(data);

  return (
    <div style={mainStyles.main}>
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
            flexDirection: "column",
            width: "100%",
            marginTop: "50px",
            background: "#FFFFFF",
            borderRadius: "10px",
            //alignItems: "center",
          }}
        >
          <div
            style={{
              marginTop: "20px",
              marginBottom: "5px",
              marginLeft: 20,
              marginRight: 10,
              color: "#625D8E",
              fontFamily: "inherit",
              fontSize: 21,
              fontWeight: "bold",
            }}
          >
            {data?.tournament.name}
          </div>

          <div
            style={{
              marginLeft: 20,
              marginRight: 10,
              color: "#7F7F7F",
              fontFamily: "inherit",
              fontSize: 18,
              //fontWeight: "bold",
            }}
          >
            {data?.tournament.venue}
          </div>

          <div
            style={{
              //marginTop: "20px",
              marginBottom: "20px",
              marginLeft: 20,
              marginRight: 10,
              color: "#7F7F7F",
              fontFamily: "inherit",
              fontSize: 18,
              //fontWeight: "bold",
            }}
          >
            Тип турнира: {data?.tournament.type.name}
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
          {data.categories
            .filter((itemF) => itemIncludes(itemF))
            .map((item) => (
              <div
                style={{ display: "flex", justifyContent: "center" }}
                key={item.category.id}
              >
                <ListItemButton key={item.category.id} sx={mainStyles.listItem}>
                  <div
                    style={{
                      display: "flex",
                      flexDirection: "row",
                      alignItems: "center",
                    }}
                  >
                    <div
                      style={{
                        display: "flex",
                        flexDirection: "column",
                        justifyContent: "center",
                        marginLeft: "20px",
                      }}
                    >
                      <div style={{ display: "flex", flexDirection: "row" }}>
                        <div
                          style={{
                            color: "#7F7F7F",
                            fontWeight: "bold",
                            fontSize: 15,
                          }}
                        >
                          Категория:
                        </div>
                        <div
                          style={{
                            color: "#719A70",
                            fontWeight: "bold",
                            fontSize: 15,
                            marginLeft: 5,
                          }}
                        >
                          {item.category.name}
                        </div>
                      </div>

                      <div style={{ display: "flex", flexDirection: "row" }}>
                        <div
                          style={{
                            color: "#7F7F7F",
                            fontWeight: "bold",
                            fontSize: 15,
                          }}
                        >
                          Место:
                        </div>
                        <div
                          style={{
                            color: "#719A70",
                            fontWeight: "bold",
                            fontSize: 15,
                            marginLeft: 5,
                          }}
                        >
                          {item.place}
                        </div>
                      </div>

                      <div style={{ display: "flex", flexDirection: "row" }}>
                        <div
                          style={{
                            color: "#7F7F7F",
                            fontWeight: "bold",
                            fontSize: 15,
                          }}
                        >
                          Присвоено очков:
                        </div>
                        <div
                          style={{
                            color: "#719A70",
                            fontWeight: "bold",
                            fontSize: 15,
                            marginLeft: 5,
                          }}
                        >
                          {item.points}
                        </div>
                      </div>
                      {/* <div style={{ color: "#7F7F7F", fontSize: 12 }}>
                        {item.category.name}
                      </div>
                      <div
                        style={{
                          color: "#7F7F7F",
                          fontWeight: "bold",
                          fontSize: 12,
                        }}
                      >
                        Всего очков: {item.points}
                      </div> */}
                    </div>
                  </div>
                </ListItemButton>
              </div>
            ))}
        </List>
      ) : null}

      <div style = {{display: "flex", flexDirection: "row"}}>
        <div
          style={{
            marginLeft: 40,
            color: "#625D8E",
            fontFamily: "inherit",
            fontSize: 21,
            fontWeight: "bold",
          }}
        >
          Итого очков:
        </div>
        <div
          style={{
            marginLeft: 5,
            color: "#719A70",
            fontFamily: "inherit",
            fontSize: 21,
            fontWeight: "bold",
          }}
        >
          {data?.points}
        </div>
      </div>
    </div>
  );
}
