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

	//infoLog := log.New(os.Stdout, "INFO\t", log.Ldate|log.Ltime)
	//errorLog := log.New(os.Stdout, "ERROR\t", log.Ldate|log.Ltime)

	router := mux.NewRouter()

	api := router.PathPrefix("/api/").Subrouter()
	// api.HandleFunc("/user/new", controllers.CreateAccount).Methods("POST")
	// api.HandleFunc("/user/login", controllers.Authenticate).Methods("POST")

	/*
		не используется
		api.HandleFunc("/contacts/new", controllers.CreateContact).Methods("POST")
		api.HandleFunc("/me/contacts", controllers.GetContactsFor).Methods("GET")
		api.HandleFunc("/inspectionGroup/new", controllers.CreateInspectionGroup).Methods("POST")
		api.HandleFunc("/me/inspectionGroup", controllers.GetInspectionGroupsFor).Methods("GET")
		api.HandleFunc("/categories/new", controllers.CreateCategory).Methods("POST")
		api.HandleFunc("/me/categories", controllers.GetСategories).Methods("GET")
	*/

	/*
		Доделать
		api.HandleFunc("/categories/new", controllers.CreateCategory).Methods("POST")
		api.HandleFunc("/me/categories", controllers.GetСategories).Methods("GET")
	*/

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

	api.HandleFunc("/category", controllers.CreateCategory).Methods("POST")
	api.HandleFunc("/category", controllers.GetСategories).Methods("GET")

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
