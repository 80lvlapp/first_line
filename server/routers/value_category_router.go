package routers

import (
	"first-line/controllers"
	"github.com/gorilla/mux"
)

func InitValueCategoryRouter(api *mux.Router) {
	api.HandleFunc("/value-category", controllers.CreateValueCategory).Methods("POST")
	api.HandleFunc("/value-category", controllers.GetValueCategores).Methods("GET")
	api.HandleFunc("/value-category/{id}", controllers.DeleteValueCategory).Methods("DELETE")
	api.HandleFunc("/value-category/{id}", controllers.UpdateValueCategory).Methods("PUT")
	api.HandleFunc("/value-category/{id}", controllers.GetValueCategory).Methods("GET")
}
