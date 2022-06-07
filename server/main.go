package main

import (
	"first-line/routers"
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
	routers.InitSchoolRouter(api)

	//Coach
	routers.InitCoachRouter(api)

	//Sportsman
	routers.InitSportsmanRouter(api)

	//TypeOfTournament
	routers.InitTypeOfTournamentRouter(api)

	//Category
	routers.InitCategoryRouter(api)

	//ValueCategory
	routers.InitValueCategoryRouter(api)

	//InfoSportsman
	routers.InitInfoSporsmanRouter(api)

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
