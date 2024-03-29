import React, { useContext, useEffect, useState } from "react";
import {
  Navigate,
  useNavigate,
  useLocation,
  useParams,
} from "react-router-dom";
import { useGetRatingSportsmanQuery } from "../../redux/apiSlice";
import { ListItemButton, List, ListItemText} from "@mui/material";
import { mainStyles } from "../../components/AppStyles";

export default function Sportsman() {
  const location = useLocation();
  let navigate = useNavigate();
  const state = location.state as CustomizedState; // Type Casting, then you can get the params passed via router
  const { idSp, idS, startDate, endDate } = useParams<{
    idSp: string;
    idS: string;
    startDate: string;
    endDate: string;
  }>();

  
  const itemIncludes = (item: any) => {
    return true;
  };

  const { data, error, isLoading } = useGetRatingSportsmanQuery({
    id: idSp !== undefined ? idSp : "",
    startDate: startDate !== undefined ? startDate : "",
    endDate: endDate !== undefined ? endDate : "",
  });

  const openTournament = (sportsman: any, tournament: any) => {
  
    navigate(
      `/AthletesRating/${idS}/Sportsman/${sportsman.id}/${startDate}/${endDate}/Tournament/${tournament.id}`,
      {
        state: { id: sportsman.id },
      }
    );
  };

  if (error) {
    return (
      <div >
        <>Oh no, there was an error</>
      </div>
    );
  } else if (isLoading) {
    return (
      <div>
        <>Loading...</>
      </div>);
  }

  console.log(data);
  

  return (
    <>
  
      {data?.map((rootItem) => (
        <div key={rootItem.sportsman.id}>
          <div
            style={{
              display: "flex",
              justifyContent: "center",
            }}
          >
            <div
              style={{
                maxWidth: "600px",
                minHeight: "70px",
                display: "flex",
                justifyContent: "space-between",
                width: "100%",
                columnGap: "5px"
              }}
            >
              <div
                style={{
              
                  background: "#FFFFFF",
                  borderRadius: "10px",
                  width: "70%",
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                  fontSize: "28px",
                  textAlign: "center",
                  minHeight:    "70px",
                  padding:"3px"
                
                }}
              >
              
                  {rootItem.sportsman.name}
               
              </div>
              <div
                style={{
                  background: "#FFFFFF",
                  borderRadius: "10px",
                  width: "30%",
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                  fontSize: "28px",
                  textAlign: "center",
                  minHeight:    "70px",
                  padding:"3px"
                }}
              >
              
                  {rootItem.points} очков
              
              </div>
            </div>
          </div>

          <List
            sx={{
              marginTop: 1
            }}
          >
            {rootItem.tournaments
              .filter((itemF) => itemIncludes(itemF))
              .map((item) => (
                <div
                 style={{ display: "flex", justifyContent: "center" }}
                  // style={{ display: "flex"}}
                  key={item.id}
                >
                  <ListItemButton
                    key={item.id}
                     onClick={(event) => {
                      openTournament(rootItem.sportsman, item);
                    }}

                    sx={mainStyles.listItem}
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
                        {item.begin_date_tournament}
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
                            color: "black",
                        
                            fontSize: 22,
                          }}
                        >
                          {item.name}
                        </div>
                        <div style={{ color: "#7F7F7F", fontSize: 12 }}>
                          {item.venue}
                        </div>
                        <div
                          style={{
                            color: "#7F7F7F",
                            fontWeight: "bold",
                            fontSize: 12,
                          }}
                        >
                          Всего очков: {item.point}
                        </div>
                      </div>
                    </div>
                  </ListItemButton>
                </div>
              ))}
          </List>
        </div>
      ))}
    </>
  );
}

interface CustomizedState {
  id: string;
}
