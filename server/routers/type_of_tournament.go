package routers

import (
	"first-line/controllers"
	"github.com/gorilla/mux"
)

func InitTypeOfTournamentRouter(api *mux.Router) {
	api.HandleFunc("/type-of-tournaments", controllers.GetTypeOfTournaments).Methods("GET")
	api.HandleFunc("/type-of-tournaments", controllers.CreateTypeOfTournament).Methods("POST")
	api.HandleFunc("/type-of-tournaments/{id}", controllers.DeleteTypeOfTournament).Methods("DELETE")
	api.HandleFunc("/type-of-tournaments/{id}", controllers.UpdateTypeOfTournament).Methods("PUT")
	api.HandleFunc("/type-of-tournaments/{id}", controllers.GetTypeOfTournaments).Methods("GET")
}
