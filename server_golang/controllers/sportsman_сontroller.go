package controllers

import (
	"encoding/json"
	"first-line/models"
	u "first-line/utils"

	"net/http"

	"github.com/gorilla/mux"
)

func CreateSportsman(w http.ResponseWriter, r *http.Request) {
	item := &models.Sportsman{}
	err := json.NewDecoder(r.Body).Decode(item)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	resp := item.CreateSportsman()
	u.Respond(w, resp)
}

func UpdateSportsman(w http.ResponseWriter, r *http.Request) {

	newItem := &models.Sportsman{}
	err := json.NewDecoder(r.Body).Decode(newItem)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.UpdateSportsman(id, *newItem)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)

}

func GetSportsmen(w http.ResponseWriter, r *http.Request) {
	data := models.GetSportsmen()
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}

func DeleteSportsman(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	resp := models.DeleteSportsman(id)
	u.Respond(w, resp)
}

func GetSportsman(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.GetSportsman(id)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}
