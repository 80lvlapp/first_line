import React, { useContext, useEffect, useState } from "react";
import {
  Navigate,
  useNavigate,
  useLocation,
  useParams,
} from "react-router-dom";
import { useGetRatingTournamentQuery } from "../../redux/apiSlice";
import { mainStyles } from "../../components/AppStyles";
import { ListItemButton, List, ListItemText } from "@mui/material";
import styles from "./Tournament.module.css";

export default function Tournament() {
  const { idSp, idT } = useParams<{ idSp: string; idT: string }>();

  const { data, error, isLoading } = useGetRatingTournamentQuery({
    id: idSp !== undefined ? idSp : "",
    idTournament: idT !== undefined ? idT : "",
  });

  const itemIncludes = (item: any) => {
    return true;
  };


  return (
    <div style={mainStyles.main}>
      {data?.map((rootItem) => (
        <div>
          {rootItem.tournaments.map((tournamentItem) => (
            <>
              <div className={styles.tournamentMain}>
                <div className={styles.tournamentColumn}>
                  <div className={styles.tournamentName}>
                    {tournamentItem.tournament.name}
                  </div>

                  <div className={styles.tournamentVenue}>
                    {tournamentItem.tournament.venue}
                  </div>

                  <div className={styles.tournamentType}>
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
                        <div className={styles.categoryRow}>
                          <div className={styles.categoryColumn}>
                            <div
                              style={{ display: "flex", flexDirection: "row" }}
                            >
                              <div className={styles.categoryTitle}>Категория:</div>

                              <div className={styles.categoryName}>
                                {categoresItem.category.name}
                              </div>
                            </div>

                            <div
                              style={{ display: "flex", flexDirection: "row" }}
                            >
                              <div className={styles.categoryPlaceTitle}>
                                Место:
                              </div>
                              <div className={styles.categoryPlace}>
                                {categoresItem.place}
                              </div>
                            </div>

                            <div
                              style={{ display: "flex", flexDirection: "row" }}
                            >
                              <div className={styles.categoryPointsTitle}>
                                Присвоено очков:
                              </div>
                              <div className={styles.categoryPoints}>
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
              <div className={styles.totalTitle}>Итого очков:</div>

              <div className={styles.total}>{rootItem.points}</div>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

