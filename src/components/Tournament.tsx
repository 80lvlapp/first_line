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
      {data?.map((rootItem) => (
        <div>
          {rootItem.tournaments.map((tournamentItem) => (
            <>
              <div style={styles.tournamentMain}>
                <div style={styles.tournamentColumn}>
                  <div style={styles.tournamentName}>
                    {tournamentItem.tournament.name}
                  </div>

                  <div style={styles.tournamentVenue}>
                    {tournamentItem.tournament.venue}
                  </div>

                  <div style={styles.tournamentType}>
                    Тип турнира:{" "}
                    {tournamentItem.tournament.type_of_tornament.name}
                  </div>
                </div>
              </div>

              <List
                sx={{
                  background: "#E5E5E5",
                  marginTop: 1,
                  marginRight: "20px",
                }}
              >
                {tournamentItem.categores
                  .filter((itemF) => itemIncludes(itemF))
                  .map((categoresItem) => (
                    <div
                      style={{ display: "flex", justifyContent: "center" }}
                      //style={{ display: "flex"}}
                      key={categoresItem.category.id}
                    >
                      <ListItemButton
                        key={categoresItem.category.id}
                        sx={mainStyles.listItem}
                      >
                        <div style={styles.categoryRow}>
                          <div style={styles.categoryColumn}>
                            <div
                              style={{ display: "flex", flexDirection: "row" }}
                            >
                              <div style={styles.categoryTitle}>Категория:</div>

                              <div style={styles.categoryName}>
                                {categoresItem.category.name}
                              </div>
                            </div>

                            <div
                              style={{ display: "flex", flexDirection: "row" }}
                            >
                              <div style={styles.categoryPlaceTitle}>
                                Место:
                              </div>
                              <div style={styles.categoryPlace}>
                                {categoresItem.place}
                              </div>
                            </div>

                            <div
                              style={{ display: "flex", flexDirection: "row" }}
                            >
                              <div style={styles.categoryPointsTitle}>
                                Присвоено очков:
                              </div>
                              <div style={styles.categoryPoints}>
                                {categoresItem.point}
                              </div>
                            </div>
                          </div>
                        </div>
                      </ListItemButton>
                    </div>
                  ))}
              </List>
            </>
          ))}

          <div
            style={{
              display: "flex",
              flexDirection: "row",
              justifyContent: "center",
            }}
          >
            <div style={{ maxWidth: "600px", width: "100%",  display: "flex", flexDirection: "row" }}>
              <div style={styles.totalTitle}>Итого очков:</div>

              <div style={styles.total}>{rootItem.points}</div>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

const styles = {
  tournamentMain: {
    display: "flex",
    justifyContent: "center",
    paddingLeft: "20px",
    paddingRight: "20px",
  },
  tournamentColumn: {
    maxWidth: "600px",
    minHeight: "70px",
    display: "flex",
    flexDirection: "column",
    width: "100%",
    marginTop: "50px",
    background: "#FFFFFF",
    borderRadius: "10px",
    //alignItems: "center",
  },
  tournamentName: {
    marginTop: "20px",
    marginBottom: "5px",
    marginLeft: 20,
    marginRight: 10,
    color: "#625D8E",
    fontFamily: "inherit",
    fontSize: 21,
    fontWeight: "bold",
  },
  tournamentVenue: {
    marginLeft: 20,
    marginRight: 10,
    color: "#7F7F7F",
    fontFamily: "inherit",
    fontSize: 18,
    //fontWeight: "bold",
  },
  tournamentType: {
    //marginTop: "20px",
    marginBottom: "20px",
    marginLeft: 20,
    marginRight: 10,
    color: "#7F7F7F",
    fontFamily: "inherit",
    fontSize: 18,
    //fontWeight: "bold",
  },
  categoryRow: {
    display: "flex",
    flexDirection: "row",
    alignItems: "center",
  },
  categoryColumn: {
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    marginLeft: "20px",
  },
  categoryTitle: {
    color: "#7F7F7F",
    fontWeight: "bold",
    fontSize: 15,
  },
  categoryName: {
    color: "#719A70",
    fontWeight: "bold",
    fontSize: 15,
    marginLeft: 5,
  },
  categoryPlaceTitle: {
    color: "#7F7F7F",
    fontWeight: "bold",
    fontSize: 15,
  },
  categoryPlace: {
    color: "#719A70",
    fontWeight: "bold",
    fontSize: 15,
    marginLeft: 5,
  },
  categoryPointsTitle: {
    color: "#7F7F7F",
    fontWeight: "bold",
    fontSize: 15,
  },
  categoryPoints: {
    color: "#719A70",
    fontWeight: "bold",
    fontSize: 15,
    marginLeft: 5,
  },
  totalTitle: {
    paddingLeft: 20,
    color: "#625D8E",
    fontFamily: "inherit",
    fontSize: 21,
    fontWeight: "bold",
  },
  total: {
    marginLeft: 5,
    color: "#719A70",
    fontFamily: "inherit",
    fontSize: 21,
    fontWeight: "bold",
  },
} as const;
