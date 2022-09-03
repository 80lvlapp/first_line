package routers

import (
	"first-line/controllers"
	"github.com/gorilla/mux"
)

func InitCategoryRouter(api *mux.Router) {
	api.HandleFunc("/category", controllers.CreateCategory).Methods("POST")
	api.HandleFunc("/category", controllers.GetCategories).Methods("GET")
	api.HandleFunc("/category/{id}", controllers.DeleteCategory).Methods("DELETE")
	api.HandleFunc("/category/{id}", controllers.UpdateCategory).Methods("PUT")
	api.HandleFunc("/category/{id}", controllers.GetCategory).Methods("GET")
}
