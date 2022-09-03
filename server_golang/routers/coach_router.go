package routers

import (
	"first-line/controllers"
	"github.com/gorilla/mux"
)

func InitCoachRouter(api *mux.Router) {
	api.HandleFunc("/coach", controllers.GetСoaches).Methods("GET")
	api.HandleFunc("/coach", controllers.CreateCoach).Methods("POST")
	api.HandleFunc("/coach/{id}", controllers.DeleteCoach).Methods("DELETE")
	api.HandleFunc("/coach/{id}", controllers.UpdateCoach).Methods("PUT")
	api.HandleFunc("/coach/{id}", controllers.GetCoach).Methods("GET")
}
