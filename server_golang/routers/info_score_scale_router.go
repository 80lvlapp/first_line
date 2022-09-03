package routers

import (
	"first-line/controllers"
	"github.com/gorilla/mux"
)

func InitInfoScoreScaleRouter(api *mux.Router) {
	api.HandleFunc("/info-score-scale-router", controllers.CreateInfoScoreScale).Methods("POST")
	api.HandleFunc("/info-score-scale-router", controllers.GetInfoScoreScales).Methods("GET")
	//api.HandleFunc("/value-category/{id}", controllers.DeleteValueCategory).Methods("DELETE")
	//api.HandleFunc("/value-category/{id}", controllers.UpdateValueCategory).Methods("PUT")
	//api.HandleFunc("/value-category/{id}", controllers.GetValueCategory).Methods("GET")
}
