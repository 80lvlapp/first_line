package controllers

import (
	"encoding/json"
	"first-line/models"
	u "first-line/utils"

	"net/http"

	"github.com/gorilla/mux"
)

func CreateTypeOfTournament(w http.ResponseWriter, r *http.Request) {
	item := &models.TypeOfTournament{}
	err := json.NewDecoder(r.Body).Decode(item)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	resp := item.CreateTypeOfTournament()
	u.Respond(w, resp)
}

func UpdateTypeOfTournament(w http.ResponseWriter, r *http.Request) {

	newItem := &models.TypeOfTournament{}
	err := json.NewDecoder(r.Body).Decode(newItem)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.UpdateTypeOfTournament(id, *newItem)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)

}

func GetTypeOfTournaments(w http.ResponseWriter, r *http.Request) {
	data := models.GetTypeOfTournaments()
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}

func DeleteTypeOfTournament(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	resp := models.DeleteTypeOfTournament(id)
	u.Respond(w, resp)
}

func GetTypeOfTournament(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.GetTypeOfTournament(id)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}
