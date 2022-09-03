package routers

import (
	"first-line/controllers"
	"github.com/gorilla/mux"
)

func InitSchoolRouter(api *mux.Router) {

	api.HandleFunc("/rest-schools", controllers.GetSchools).Methods("GET")
	api.HandleFunc("/rest-schools", controllers.CreateSchool).Methods("POST")
	api.HandleFunc("/rest-schools/{id}", controllers.DeleteSchool).Methods("DELETE")
	api.HandleFunc("/rest-schools/{id}", controllers.UpdateSchool).Methods("PUT")

	api.HandleFunc("/rest-schools/{id}", controllers.GetSchool).Methods("GET")

	api.HandleFunc("/rest-schools", controllers.GetSchools).Methods("GET")
	api.HandleFunc("/rest-schools", controllers.GetSchoolsLikeName).Queries("name", "{name}").Methods("GET")
	//api.HandleFunc("/rest-schools", controllers.GetSchools).Queries("address", "{address}").Methods("GET")
	//api.HandleFunc("/rest-schools", controllers.GetSchools).Queries("name", "{name}", "address", "{address}").Methods("GET")
}
