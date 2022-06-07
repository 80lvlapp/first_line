package controllers

import (
	"encoding/json"
	"first-line/models"
	u "first-line/utils"

	"net/http"

	"github.com/gorilla/mux"
)

func CreateTournament(w http.ResponseWriter, r *http.Request) {
	item := &models.Tournament{}
	err := json.NewDecoder(r.Body).Decode(item)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	resp := item.CreateTournament()
	u.Respond(w, resp)
}

func UpdateTournament(w http.ResponseWriter, r *http.Request) {

	newItem := &models.Tournament{}
	err := json.NewDecoder(r.Body).Decode(newItem)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.UpdateTournament(id, *newItem)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)

}

func GetTournaments(w http.ResponseWriter, r *http.Request) {
	data := models.GetTournaments()
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}

func DeleteTournament(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	resp := models.DeleteTournament(id)
	u.Respond(w, resp)
}

func GetTournament(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.GetTournament(id)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}
