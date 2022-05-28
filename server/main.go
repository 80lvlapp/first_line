package main

import (
	"fmt"
	"go-contacts/controllers"
	//	"go-contacts/app"
	//	"go-contacts/controllers"
	"net/http"
	"os"

	//	"path"
	//	"strings"

	"github.com/gorilla/mux"
)

const FSPATH = "./webClient/build/static/index.html"

func main() {

	router := mux.NewRouter()

	api := router.PathPrefix("/api/").Subrouter()
	api.HandleFunc("/user/new", controllers.CreateAccount).Methods("POST")
	api.HandleFunc("/user/login", controllers.Authenticate).Methods("POST")
	api.HandleFunc("/contacts/new", controllers.CreateContact).Methods("POST")
	api.HandleFunc("/me/contacts", controllers.GetContactsFor).Methods("GET")
	api.HandleFunc("/inspectionGroup/new", controllers.CreateInspectionGroup).Methods("POST")
	api.HandleFunc("/me/inspectionGroup", controllers.GetInspectionGroupsFor).Methods("GET")
	api.HandleFunc("/categories/new", controllers.CreateCategory).Methods("POST")
	api.HandleFunc("/me/categories", controllers.GetСategories).Methods("GET")
	


	//router.PathPrefix("/static/").Handler(http.StripPrefix("/static/", http.FileServer(http.Dir("./build/static/"))))

	//router.PathPrefix("/").HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
	//	http.ServeFile(w, r, "./build/index.html")
	//})

	router.Use(accessControlMiddleware);
	
	//router.Use(app.JwtAuthentication) //attach JWT auth middleware

	port := os.Getenv("PORT")
	if port == "" {
		port = "8000" //localhost
	}

	fmt.Println(port)

	err := http.ListenAndServe(":"+port, router) //Launch the app, visit localhost:8000/api
	if err != nil {
		fmt.Print(err)
	}
	
	

}

func accessControlMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Access-Control-Allow-Origin", "*")
		w.Header().Set("Access-Control-Allow-Methods", "GET, POST, OPTIONS,PUT")
		w.Header().Set("Access-Control-Allow-Headers", "Origin, Content-Type")

		if r.Method == "OPTIONS" {
			return
		}

		next.ServeHTTP(w, r)
	})
}
