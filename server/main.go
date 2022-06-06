package main

import (
	"first-line/controllers"
	"fmt"
	"github.com/gorilla/mux"
	"net/http"
	"os"
)

const FSPATH = "./webClient/build/static/index.html"

func main() {

	router := mux.NewRouter()

	api := router.PathPrefix("/api/").Subrouter()

	//School
	api.HandleFunc("/rest-schools", controllers.GetSchools).Methods("GET")
	api.HandleFunc("/rest-schools", controllers.CreateSchool).Methods("POST")
	api.HandleFunc("/rest-schools/{id}", controllers.DeleteSchool).Methods("DELETE")
	api.HandleFunc("/rest-schools/{id}", controllers.UpdateSchool).Methods("PUT")
	api.HandleFunc("/rest-schools/{id}", controllers.GetSchool).Methods("GET")

	//Coach
	api.HandleFunc("/coach", controllers.GetСoaches).Methods("GET")
	api.HandleFunc("/coach", controllers.CreateCoach).Methods("POST")
	api.HandleFunc("/coach/{id}", controllers.DeleteCoach).Methods("DELETE")
	api.HandleFunc("/coach/{id}", controllers.UpdateCoach).Methods("PUT")
	api.HandleFunc("/coach/{id}", controllers.GetCoach).Methods("GET")

	//Sportsman
	api.HandleFunc("/sportsmen", controllers.GetSportsmen).Methods("GET")
	api.HandleFunc("/sportsmen", controllers.CreateSportsman).Methods("POST")
	api.HandleFunc("/sportsmen/{id}", controllers.DeleteSportsman).Methods("DELETE")
	api.HandleFunc("/sportsmen/{id}", controllers.UpdateSportsman).Methods("PUT")
	api.HandleFunc("/sportsmen/{id}", controllers.GetSportsman).Methods("GET")

	//TypeOfTournament
	api.HandleFunc("/type-of-tournaments", controllers.GetTypeOfTournaments).Methods("GET")
	api.HandleFunc("/type-of-tournaments", controllers.CreateTypeOfTournament).Methods("POST")
	api.HandleFunc("/type-of-tournaments/{id}", controllers.DeleteTypeOfTournament).Methods("DELETE")
	api.HandleFunc("/type-of-tournaments/{id}", controllers.UpdateTypeOfTournament).Methods("PUT")
	api.HandleFunc("/type-of-tournaments/{id}", controllers.GetTypeOfTournaments).Methods("GET")

	//Category
	api.HandleFunc("/category", controllers.CreateCategory).Methods("POST")
	api.HandleFunc("/category", controllers.GetCategories).Methods("GET")
	api.HandleFunc("/category/{id}", controllers.DeleteCategory).Methods("DELETE")
	api.HandleFunc("/category/{id}", controllers.UpdateCategory).Methods("PUT")
	api.HandleFunc("/category/{id}", controllers.GetCategory).Methods("GET")

	//ValueCategory
	api.HandleFunc("/value-category", controllers.CreateValueCategory).Methods("POST")
	api.HandleFunc("/value-category", controllers.GetValueCategores).Methods("GET")
	api.HandleFunc("/value-category/{id}", controllers.DeleteValueCategory).Methods("DELETE")
	api.HandleFunc("/value-category/{id}", controllers.UpdateValueCategory).Methods("PUT")
	api.HandleFunc("/value-category/{id}", controllers.GetValueCategory).Methods("GET")

	//InfoSportsman
	api.HandleFunc("/info-sportsman", controllers.CreateInfoSportsman).Methods("POST")
	api.HandleFunc("/info-sportsman", controllers.GetInfoSportsmen).Methods("GET")
	//api.HandleFunc("/value-category/{id}", controllers.DeleteValueCategory).Methods("DELETE")
	//api.HandleFunc("/value-category/{id}", controllers.UpdateValueCategory).Methods("PUT")
	//api.HandleFunc("/value-category/{id}", controllers.GetValueCategory).Methods("GET")

	router.Use(accessControlMiddleware)

	port := os.Getenv("PORT")
	if port == "" {
		port = "8000" //localhost
	}
	fmt.Println(port)
	//infoLog.Printf("Запуск сервера на %s", )

	err := http.ListenAndServe(":"+port, router) //Launch the app, visit localhost:8000/api
	if err != nil {
		fmt.Print(err)

	}
}

func accessControlMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Access-Control-Allow-Origin", "*")
		w.Header().Set("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT")
		w.Header().Set("Access-Control-Allow-Headers", "Origin, Content-Type")

		if r.Method == "OPTIONS" {
			return
		}

		next.ServeHTTP(w, r)
	})
}
