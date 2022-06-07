package routers

import (
	"first-line/controllers"
	"github.com/gorilla/mux"
)

func InitSportsmanRouter(api *mux.Router) {
	api.HandleFunc("/sportsmen", controllers.GetSportsmen).Methods("GET")
	api.HandleFunc("/sportsmen", controllers.CreateSportsman).Methods("POST")
	api.HandleFunc("/sportsmen/{id}", controllers.DeleteSportsman).Methods("DELETE")
	api.HandleFunc("/sportsmen/{id}", controllers.UpdateSportsman).Methods("PUT")
	api.HandleFunc("/sportsmen/{id}", controllers.GetSportsman).Methods("GET")
}
