package school

import (
	"github.com/gorilla/mux"
)

func InitSchoolRouter(api *mux.Router) {
	api.HandleFunc("/rest-schools", GetSchools).Methods("GET")
	api.HandleFunc("/rest-schools", CreateSchool).Methods("POST")
	api.HandleFunc("/rest-schools/{id}", DeleteSchool).Methods("DELETE")
	api.HandleFunc("/rest-schools/{id}", UpdateSchool).Methods("PUT")
	api.HandleFunc("/rest-schools/{id}", GetSchool).Methods("GET")
}
