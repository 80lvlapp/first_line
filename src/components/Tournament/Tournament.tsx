import React, { useContext, useEffect, useState } from "react";
import {
  useParams,
} from "react-router-dom";
import { useGetRatingTournamentQuery } from "../../redux/apiSlice";
import { mainStyles } from "../../components/AppStyles";
import { List, ListItem } from "@mui/material";
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
    <div className={styles.page}>
      {data && <div className={styles.content}>

       <div className={styles.tournamentCardContent}>

          <div className={styles.tournamentName}>
            {data[0].tournaments[0].name}
          </div>

          <div className={styles.characteristicsTournament}>

            <div className={styles.tournamentVenue}>

              <div className={styles.tournamentVenueTitle}>
                город:
              </div>

              <div className={styles.tournamentVenueValue}>
                {data[0].tournaments[0].venue}
              </div>

            </div>

            <div className={styles.tournamentType}>

              <div className={styles.tournamentTypeTitle}>
                тип турнира:
              </div>

              <div className={styles.tournamentTypeValue}>
                {data[0].tournaments[0].type_of_tornament.name}
              </div>
            </div>

          </div>
        </div>


        <List
          sx={{
            marginTop: 1
          }}
        >
          {data[0].tournaments[0].categores.map((categoresItem) => (
            <div
              key={categoresItem.category.id.toString()}
              style={{ display: "flex", justifyContent: "center" }}

            >
              <ListItem

                sx={mainStyles.listItem}
              >
                <div className={styles.categoryRow}>
                  <div className={styles.categoryColumn}>
                    <div
                      style={{ display: "flex", flexDirection: "row" }}
                    >
                      <div className={styles.categoryTitle}>
                        Категория:
                      </div>

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
                      style={{display: "flex", flexDirection: "row" }}
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
              </ListItem>
            </div>
          ))}
        </List>


        <div key={'total'}
          style={{
            display: "flex",
            flexDirection: "row",
            justifyContent: "center",
          }}
        >
          <div className={styles.total}>
            <div className={styles.totalTitle}>Итого очков:</div>
            <div className={styles.totalValue}>{data[0].points}</div>
          </div>
        </div>

      </div>}
    </div >
  );
}

