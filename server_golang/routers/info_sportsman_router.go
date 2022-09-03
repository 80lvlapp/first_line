package routers

import (
	"first-line/controllers"
	"github.com/gorilla/mux"
)

func InitInfoSporsmanRouter(api *mux.Router) {
	api.HandleFunc("/info-sportsman", controllers.CreateInfoSportsman).Methods("POST")
	api.HandleFunc("/info-sportsman", controllers.GetInfoSportsmen).Methods("GET")
	//api.HandleFunc("/value-category/{id}", controllers.DeleteValueCategory).Methods("DELETE")
	//api.HandleFunc("/value-category/{id}", controllers.UpdateValueCategory).Methods("PUT")
	//api.HandleFunc("/value-category/{id}", controllers.GetValueCategory).Methods("GET")
}
