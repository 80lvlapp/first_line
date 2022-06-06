package controllers

import (
	"encoding/json"
	"first-line/models"
	u "first-line/utils"

	"net/http"

	"github.com/gorilla/mux"
)

func CreateInfoSportsman(w http.ResponseWriter, r *http.Request) {
	item := &models.InfoSportsman{}
	err := json.NewDecoder(r.Body).Decode(item)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	resp := item.CreateInfoSportsman()
	u.Respond(w, resp)
}

func UpdateInfoSportsman(w http.ResponseWriter, r *http.Request) {

	newItem := &models.InfoSportsman{}
	err := json.NewDecoder(r.Body).Decode(newItem)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.UpdateInfoSportsman(id, *newItem)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)

}

func GetInfoSportsmen(w http.ResponseWriter, r *http.Request) {
	data := models.GetInfoSportsmen()
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}

func DeleteInfoSportsman(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	resp := models.DeleteInfoSportsman(id)
	u.Respond(w, resp)
}

func GetInfoSportsman(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.GetInfoSportsman(id)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}
