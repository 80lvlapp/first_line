package routers

import (
	"first-line/controllers"
	"github.com/gorilla/mux"
)

func InitTournamentRouter(api *mux.Router) {
	api.HandleFunc("/tournaments", controllers.GetTournaments).Methods("GET")
	api.HandleFunc("/tournaments", controllers.CreateTournament).Methods("POST")
	api.HandleFunc("/tournaments/{id}", controllers.DeleteTournament).Methods("DELETE")
	api.HandleFunc("/tournaments/{id}", controllers.UpdateTournament).Methods("PUT")
	api.HandleFunc("/tournaments/{id}", controllers.GetTournament).Methods("GET")
}
